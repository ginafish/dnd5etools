import json



class CharacterSheet:
    def __init__(self, name):
        with open('./' + name + '/stats.json') as characterSheetFile:
            self.characterSheetJson = json.load(characterSheetFile)

        with open('./characterSheetRequirements.json') as characterSheetRequirementsFile:
            self.characterSheetRequirements = json.load(characterSheetRequirementsFile)

        for field in range(0, len(self.characterSheetRequirements)):

        # -------------- Verify mandatory fields present --------------
        if "Character Name" not in self.characterSheetJson:
            raise ValueError('\"Character Name\" not set in selected character sheet.')


        # -------------- Show warning for recommended fields being missing --------------
        if "Character Name" not in self.characterSheetJson:
            print unicode('\"Character Name\" not set in selected character sheet.')
        if "Class" not in self.characterSheetJson:
            print unicode('\"Class\" not set in selected character sheet.')



    def getCharacterName(self):
        return self.characterSheetJson["Character Name"]

    def getCharacterClass(self):
        return self.characterSheetJson["Class"]

    def getCharacterExp(self):
        return self.characterSheetJson["Exp"]

    def getCharacterLevel(self):
        return self.characterSheetJson["Level"]

    def getCharacterRace(self):
        return self.characterSheetJson["Race"]

    def getCharacterAlignment(self):
        return self.characterSheetJson["Alignment"]

    def getCharacterAge(self):
        return self.characterSheetJson["Age"]

    def getCharacterGender(self):
        return self.characterSheetJson["Gender"]

    def getCharacterHeight(self):
        return self.characterSheetJson["Height"]

    def getCharacterWeight(self):
        return self.characterSheetJson["Weight"]

    def getCharacterEyes(self):
        return self.characterSheetJson["Eyes"]

    def getCharacterSkin(self):
        return self.characterSheetJson["Skin"]

    def getCharacterHair(self):
        return self.characterSheetJson["Hair"]

    def getCharacterStr(self):
        return self.characterSheetJson["Base Stats"]["STR"]

    def getCharacterDex(self):
        return self.characterSheetJson["Base Stats"]["DEX"]

    def getCharacterCon(self):
        return self.characterSheetJson["Base Stats"]["CON"]

    def getCharacterInt(self):
        return self.characterSheetJson["Base Stats"]["INT"]

    def getCharacterWis(self):
        return self.characterSheetJson["Base Stats"]["WIS"]

    def getCharacterChr(self):
        return self.characterSheetJson["Base Stats"]["CHR"]

    def getCharacterBaseStats(self):
        return unicode("STR: " + self.getCharacterStr() + "\nDEX: " + self.getCharacterDex() +
                       "\nCON: " + self.getCharacterCon() + "\nINT: " + self.getCharacterInt() +
                       "\nWIS: " + self.getCharacterWis() + "\nCHR: " + self.getCharacterChr())

    def getCharacterProficiencyBonus(self):
        return self.characterSheetJson["Proficiency Bonus"]

    def getCharacterSpeed(self):
        return self.characterSheetJson["Speed"]

    def getCharacterMaxHP(self):
        return self.characterSheetJson["Max HP"]


