import json
import re

import main.rollSkill
#from pprint import pprint


def doRollSkill(skill):
    parsedSkill = re.sub(r"^(roll )", '', playerCommand)
    parsedSkill = re.sub(r"( check)", '', parsedSkill)
    #print("DEBUG: parsedSkill = " + parsedSkill)
    main.rollSkill.rollSkill(parsedSkill, characterSheet)



characterName = raw_input('Please enter the character you are using: \n: ')
with open('characters/' + characterName + '/stats.json') as characterSheetFile:
    characterSheet = json.load(characterSheetFile)


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


playerCommand = raw_input('What would you like to do?\n' +
                      'roll [skill] check\n\n' +
                      ': ')

rollSkillCheckRegex = re.compile(r"^(roll) \w+ (check)")

if(rollSkillCheckRegex.match(playerCommand)):
    doRollSkill(playerCommand)




