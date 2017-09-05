import json
import re

import main.rollSkill
#from pprint import pprint


characterName = raw_input('Please enter the name of the character to select in lowercase: \n: ')
with open('characters/' + characterName + '/stats.json') as characterSheetFile:
    characterSheet = json.load(characterSheetFile)



# --------------------------------------------------------
def parseRollCheck(command):
    parsedSkill = re.sub(r"^(roll )", '', command)
    parsedSkill = re.sub(r"( check)", '', parsedSkill)
    return parsedSkill


def doRollSkill(skill, characterSheet = characterSheet):
    main.rollSkill.rollSkill(skill, characterSheet)


def printCommandList():
    print "roll [Skill Name] check\n\n"


def getPlayerCommand():
    playerCommand = raw_input('What would you like to do?\n' + ': ')

    rollSkillCheckRegex = re.compile(r"^(roll) \w+ (check)")
    helpRegex = re.compile(r"^(help)")
    quitRegex = re.compile(r"^(exit|quit)")

    if(rollSkillCheckRegex.match(playerCommand)):
        parsedSkill = parseRollCheck(playerCommand)
        doRollSkill(parsedSkill)
    elif(helpRegex.match(playerCommand)):
        printCommandList()
    elif(quitRegex.match(playerCommand)):
        raise SystemExit

# --------------------------------------------------------



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
print unicode(characterInfo)

while(True):
    getPlayerCommand()



