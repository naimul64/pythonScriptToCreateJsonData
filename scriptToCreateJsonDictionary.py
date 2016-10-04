import random
from enum import Enum

class CharOption(Enum):
    Alpha = "Alpha"
    Numeric = "Numeric"
    AlphaNumeric = "AlphaNumeric"

noOfScanBySingleScanner = 1000;
def createNID():
    return "12345678901234567"

def getRandomConfidence():
    return random.randrange(50, 100)

def getVowelAsString():
    i = random.randrange(0,5)
    return ["a","e","i","o","u"][i];

def getConsonentAsString(mode):
    while (1):
        i = random.randrange(0,25);
        if(i not in [0,4,8,14,20]):
            if(mode == 'caps'):
                char = chr(i + 65);
            else:
                char = chr(i + 97);
            return str(char);


def prepareName():
    name = ""
    for i in range(0,10):
        if(i==5):
            name += " "
            continue
        elif i%2 == 0:
            if(i == 0 or i == 6 ):
                name += getConsonentAsString("caps");
            else:
                name += getConsonentAsString("small");
        else:
            name += getVowelAsString();

    return name;

def getScannerId(index):
    scannerId = "s1psl";
    scannerId += str(int(index/noOfScanBySingleScanner) + 1);
    return scannerId;

def getSeq(index):
    return (index%noOfScanBySingleScanner + 1);

def getSrcFileName():
    return "rotate.pdf";

def getFullImg():
    return "rotate.pdf";

def getimgPath():
    return "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Einstein_Szilard_p1.jpg/220px-Einstein_Szilard_p1.jpg"

def getStatus():
    return "PROCESSED"

def createNameOrCodeByRandomization(length, builderCharacterType):
    index = 0;
    codeOrNameString = ""
    while index < length:
        if builderCharacterType == "Alpha":
            rand = random.randrange(0,25)
            codeOrNameString += str(chr(65+rand));
        elif builderCharacterType == "Numeric":
            rand = random.randrange(0,9)
            codeOrNameString += str(chr(48+rand));
        index = index + 1
    return codeOrNameString;

def createValScoreDic(char):
    dic = {}
    dic['val'] = char
    dic['score'] = getRandomConfidence();
    return dic;


def getIcrCharListFromOriginal(original):
    valScoreDicList = []
    for index in range(0,len(original)):
        char = original[index : index+1]
        valScoreDicList.append(createValScoreDic(char))
    return valScoreDicList

def getIcrcharImgpathOriginalDic(length, charOption):
    innderDictionary = {}
    innderDictionary['original'] = createNameOrCodeByRandomization(length, charOption);
    innderDictionary['imgPath'] = getimgPath();
    innderDictionary['icrChars'] = getIcrCharListFromOriginal(innderDictionary['original']);
    return innderDictionary

def getSchoolCode(length, charOptioin):
    localDictionary = {}
    localDictionary['value'] = getIcrcharImgpathOriginalDic(length, charOptioin);
    return localDictionary;

for index in range(0, 1000):
    dictionary = {"_class" : "com.progoti.kycreader.server.core.domains.DisbursementSheet"}
    dictionary['scannerId'] = getScannerId(index);
    dictionary['seq'] = getSeq(index);
    dictionary['srcFileName'] = getSrcFileName()
    dictionary['fullImg'] = getFullImg();
    dictionary['status'] = getStatus();
    dictionary['schoolCode'] = getSchoolCode(12, CharOption.Numeric);

    print dictionary;