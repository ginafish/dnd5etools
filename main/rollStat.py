import json
import random


def isValidStat(testStat):
    statShortList = ["STR", "CON", "DEX", "WIS", "INT", "CHR"]
    for statName in statShortList:
        if(statName == testStat.upper()):
            return True
    return False

def rollStatCheck(statRoll, characterSheet):
    stat = statRoll.upper()
    if(not isValidStat(stat)):
        print 'Invalid stat ' + statRoll + '\n'
        return -1

    statModifier = 0
    if (stat in characterSheet["Base Stats"]):
        statModifier = (characterSheet["Base Stats"][stat] - 10) // 2
    else:
        print "ERROR: Character sheet is missing your " + unicode(stat) + " stat, or is not properly formatted.\n"
        raise SystemExit

    random.seed()
    roll = random.randint(1, 20)
    result = roll + statModifier

    print unicode(characterSheet["Character Name"]) + \
          " rolled a " + unicode(result) + \
          " on their " + unicode(stat) + " check.\n" + \
          "(roll: " + unicode(roll) + \
          ", modifier: " + unicode(statModifier) + ")\n"
    return result
