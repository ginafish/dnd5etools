import re
import json
import random

import rollSkill
import rollStat



# --------------------------------------------------------
def setCharacterSheet():
    characterName = raw_input('Please enter the name of the character to select (not case sensitive): \n: ')
    try:
        with open('main/characterSheets/' + characterName + '/stats.json', 'r+') as characterSheetFile:
            characterSheet = json.load(characterSheetFile)
        characterSheetFile.close()
        return characterSheet
    except IOError:
        print('Invalid character sheet.\n')
        return None

def buildCharacterInfo():
    characterName = characterSheet["Character Name"]
    characterRace = characterSheet["Race"]
    characterClass = characterSheet["Class"]
    characterLevel = characterSheet["Level"]
    characterExp = characterSheet["Exp"]
    characterInfo = "\n Selected character:\n" + unicode(characterName) + ", " \
                    + unicode(characterRace) + " " \
                    + unicode(characterClass) + ", Level " \
                    + unicode(characterLevel) + ", EXP: " \
                    + unicode(characterExp) + "\n"
    return characterInfo


def parseRollCheck(command):
    parsedRoll = re.sub(r"^(roll )", '', command)
    parsedRoll = re.sub(r"( check)", '', parsedRoll)
    return parsedRoll

def doRollSkill(skill, characterSheet):
    rollSkill.rollSkillCheck(skill, characterSheet)

def doRollStat(stat, characterSheet):
    rollStat.rollStatCheck(stat, characterSheet)



def doCurrentHealthCheck(characterSheet):
    print "Your current health is " + \
          unicode(characterSheet["Current HP"]) + \
          " out of " + \
          unicode(characterSheet["Max HP"])


def printCharacterInfo():
    info = buildCharacterInfo()
    print unicode(info)


def printCommandList():
    commandList = "------ Command list ------\n" + \
          "help\n" + \
          "roll [Skill Name] check\n" + \
          "roll [Stat] check\n" + \
          "roll [die]\n" + \
          "take [amount] damage\n" + \
          "gain exp\n" \
          "current health\n" + \
          "[quit | exit]\n" + \
          "--------------------------\n"
    print commandList
    return commandList


def getPlayerCommand():
    playerCommand = raw_input('What would you like to do?\n' + ': ')

    helpRegex = re.compile(r"^(help)")
    rollCheckRegex = re.compile(r"^(roll) \w+ *\w* (check)")
    quitRegex = re.compile(r"^(exit|quit)")

    if(rollCheckRegex.match(playerCommand)):
        parsedRoll = parseRollCheck(playerCommand)
        if(rollSkill.isValidSkill(parsedRoll)):
            doRollSkill(parsedRoll, characterSheet)
        elif(rollStat.isValidStat(parsedRoll)):
            doRollStat(parsedRoll, characterSheet)
        else:
            print 'Invalid roll.  If you\'re not sure what to do, try entering \'help\'.\n'
    elif(helpRegex.match(playerCommand)):
        printCommandList()
    elif(quitRegex.match(playerCommand)):
        print "Goodbye!"
        raise SystemExit
    else:
        print "Invalid command.  If you\'re not sure what to do, try entering \'help\'.\n"


# --------------------------------------------------------

characterSheet = setCharacterSheet()

while(characterSheet == None):
    characterSheet = setCharacterSheet()

printCharacterInfo()

random.seed()

while(True):
    getPlayerCommand()



