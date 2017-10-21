import json
import random

#TODO: make case insensitive
def isValidSkill(testSkill):
    with open('main/data/skillsList.json') as skillsFile:
        skillsList = json.load(skillsFile)
    for skill in skillsList:
        #print unicode(skill["Name"]) + " " + unicode(skill["Name"] == testSkill) + " " + skill["Name"]
        if(skill["Name"] == testSkill):
            return True
    return False


def rollSkillCheck(rolledSkill, characterSheet):
    if(not isValidSkill(rolledSkill)):
        print("Invalid skill roll.\n")
        return -1

    with open('main/data/skillsList.json') as skillsFile:
        skillsList = json.load(skillsFile)

    appliedProficiencyBonus = 0
    if (rolledSkill in characterSheet["Skill Proficiencies"]):
        appliedProficiencyBonus = characterSheet["Proficiency Bonus"]

    skillModifier = 0
    for skill in skillsList:
        if (skill["Name"] == rolledSkill):
            skillValue = characterSheet["Base Stats"][unicode(skill["Stat"])]
            skillModifier = ((skillValue - 10) // 2)

    roll = random.randint(1, 20)
    result = roll + appliedProficiencyBonus + skillModifier
    print unicode(characterSheet["Character Name"]) + \
          " rolled a " + unicode(result) + \
          " on their " + unicode(rolledSkill) + " check.\n" + \
          "(roll: " + unicode(roll) + \
          ", skill modifier: " + unicode(skillModifier) + \
          ", proficiency bonus: " + unicode(appliedProficiencyBonus) + ")\n"
    return result


def printSkillList():
    with open('skills/skillsList.json') as skillsFile:
        skillsList = json.load(skillsFile)
    for skill in skillsList:
        print(skill["Name"])


