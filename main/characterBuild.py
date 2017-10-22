import random
import json

def rollStatRolls(newCharacterSheet):
    NUM_SCORES = 6
    NUM_SCORE_ROLLS = 4

    abilityScoreRolls = [[0 for x in range(NUM_SCORE_ROLLS)] for x in range(NUM_SCORES)]
    abilityScoreRollsSums = [0 for x in range(NUM_SCORES)]

    #do rolls
    for j in range(NUM_SCORES):
        for i in range(NUM_SCORE_ROLLS):
            abilityScoreRolls[j][i] = random.randint(1, 6)
    print abilityScoreRolls

    #remove lowest roll from each roll list and print sum
    for k in range(NUM_SCORES):
        abilityScoreRolls[k].remove(min(abilityScoreRolls[k]))
        abilityScoreRollsSums[k] = sum(abilityScoreRolls[k])
        print "Roll " + unicode(k) + ": " + unicode(abilityScoreRollsSums[k]) + '\n'
    print abilityScoreRolls
    

    # newCharacterSheet["Base Stats"] = {}

    # #for i in range(NUM_SCORES):
    # chosenStat = raw_input("Please enter the index you would like to choose your STR Stat:\n$ ")
    # newCharacterSheet["Base Stats"]["STR"] = 


    # newCharacterSheet["Base Stats"]["DEX"] = 0
    # newCharacterSheet["Base Stats"]["CON"] = 0
    # newCharacterSheet["Base Stats"]["INT"] = 0
    # newCharacterSheet["Base Stats"]["WIS"] = 0
    # newCharacterSheet["Base Stats"]["CHR"] = 0


newCharacterSheet = {}
rollStatRolls(newCharacterSheet)
