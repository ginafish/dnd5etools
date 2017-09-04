import json
import random

def isValidSkill(testSkill):
    with open('skills/skills.json') as skillsFile:
        skillsList = json.load(skillsFile)
    for skill in skillsList:
        if(skill["Name"] == testSkill):
            return True
    return False


def rollSkill(rolledSkill, characterSheet):
    if(not isValidSkill(rolledSkill)):
        print("Invalid skill roll.")
        return -1

    with open('skills/skills.json') as skillsFile:
        skillsList = json.load(skillsFile)

    appliedProficiencyBonus = 0
    if (rolledSkill in characterSheet["Skill proficiencies"]):
        appliedProficiencyBonus = characterSheet["Proficiency Bonus"]

    skillModifier = 0
    for skill in skillsList:
        if (skill["Name"] == rolledSkill):
            skillValue = characterSheet["Base Stats"][unicode(skill["Stat"])]
            skillModifier = ((skillValue - 10) // 2)

    random.seed()
    roll = random.randint(1, 20)
    result = roll + appliedProficiencyBonus + skillModifier
    print unicode(characterSheet["Character Name"]) + \
    " rolled a " + unicode(result) + \
    " on their " + unicode(rolledSkill) + " check."


def printSkillList():
    with open('skills/skills.json') as skillsFile:
        skillsList = json.load(skillsFile)
    for skill in skillsList:
        print(skill["Name"])


