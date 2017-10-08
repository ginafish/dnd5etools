import re
import json

import main.rollSkill
#from pprint import pprint





# --------------------------------------------------------
def setCharacterSheet():
    characterName = raw_input('Please enter the name of the character to select (not case sensitive): \n: ')
    with open('characterSheets/' + characterName + '/stats.json') as characterSheetFile:
        characterSheet = json.load(characterSheetFile)
    return characterSheet


def parseSkillRollCheck(command):
    parsedSkill = re.sub(r"^(roll )", '', command)
    parsedSkill = re.sub(r"( check)", '', parsedSkill)
    print parsedSkill
    return parsedSkill

def doRollSkill(skill, characterSheet):
    main.rollSkill.rollSkillCheck(skill, characterSheet)


def doCurrentHealthCheck(characterSheet):
    print "Your current health is " + \
          unicode(characterSheet["Current HP"]) + \
          " out of " + \
          unicode(characterSheet["Max HP"])


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
    rollSkillCheckRegex = re.compile(r"^(roll) \w+ *\w* (check)")
    quitRegex = re.compile(r"^(exit|quit)")

    if(rollSkillCheckRegex.match(playerCommand)):
        parsedSkill = parseSkillRollCheck(playerCommand)
        doRollSkill(parsedSkill, characterSheet)
    elif(helpRegex.match(playerCommand)):
        printCommandList()
    elif(quitRegex.match(playerCommand)):
        print "Goodbye!"
        raise SystemExit
    else:
        print "Invalid command.\n"


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


def printCharacterInfo():
    info = buildCharacterInfo()
    print unicode(info)


# --------------------------------------------------------

characterSheet = setCharacterSheet()

printCharacterInfo()

while(True):
    getPlayerCommand()



