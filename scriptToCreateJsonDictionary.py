import random
from enum import Enum

noOfEntryInDS = 2
noOfScanBySingleScanner = 1;
totalRowToCreate = 1;

class CharOption(Enum):
    Alpha = "Alpha"
    Numeric = "Numeric"
    AlphaNumeric = "AlphaNumeric"

def createNID():
    return "12345678901234567"

def getRandomConfidence():
    return random.randrange(50, 100)

def getVowelAsString(mode):
    if mode == 'caps':
        i = random.randrange(0,5)
        return ["A","E","I","O","U"][i];
    else:
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


def prepareFullName(min, max):
    name = ""
    for i in range(min,max):
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

def prepareSingleNameInCaps(min, max):
    name = ""
    for i in range(min,max):
        if i%2 == 0:

            name += getConsonentAsString("caps");
        else:
            name += getVowelAsString('caps');

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
    return "rotate_2016_09_14_11_39_03/SCHOOL_CODE.png"

def getStatus():
    return "PROCESSED"

def createNameOrCodeByRandomization(length, builderCharacterType):
    index = 0;
    codeOrNameString = ""
    if builderCharacterType == CharOption.Numeric:
        while index < length:
            rand = random.randrange(0,9)
            codeOrNameString += str(chr(48+rand));
            index = index + 1
        return codeOrNameString;
        
    if builderCharacterType == CharOption.Alpha:
        codeOrNameString += prepareSingleNameInCaps(0, length)
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

def getIcrcharImgPath(innderDictionary):
    innderDictionary['imgPath'] = getimgPath();
    innderDictionary['icrChars'] = getIcrCharListFromOriginal(innderDictionary['original']);


def getIcrcharImgpathOriginalDic(length, charOption):
    innderDictionary = {}
    innderDictionary['original'] = createNameOrCodeByRandomization(length, charOption);

    getIcrcharImgPath(innderDictionary)

    return innderDictionary

def getIcrcharImgpathOriginalDicForMobileNo(length, charOption):
    innderDictionary = {}
    mobileNoPrefix = ['015','016','017','018','019'][random.randrange(0,4)]
    innderDictionary['original'] = mobileNoPrefix + createNameOrCodeByRandomization(8, charOption);

    getIcrcharImgPath(innderDictionary)

    return innderDictionary

def getIcrcharImgpathOriginalDicForAmount(stdCount):
    innderDictionary = {}
    if(stdCount == '1'):
        innderDictionary['original'] = '1200';
    elif (stdCount == '2'):
        innderDictionary['original'] = '2400';
    elif (stdCount == '3'):
        innderDictionary['original'] = '3000';
    else:
        innderDictionary['original'] = '3600';

    getIcrcharImgPath(innderDictionary)

    return innderDictionary


def getIcrcharImgpathOriginalDicForStdcount(length, charOption):
    innderDictionary = {}
    innderDictionary['original'] = str(random.randrange(1,6))

    getIcrcharImgPath(innderDictionary)

    return innderDictionary


def getSchoolCode(length, charOptioin):
    localDictionary = {}
    localDictionary['value'] = getIcrcharImgpathOriginalDic(length, charOptioin);
    return localDictionary;

def createDataDic(index):
    dataDic = {}
    dataDic['slNo'] = getIcrcharImgpathOriginalDic(3,CharOption.Numeric);
    dataDic['name'] = getIcrcharImgpathOriginalDic(random.randrange(6,8),CharOption.Alpha);
    dataDic['mobile'] = getIcrcharImgpathOriginalDicForMobileNo(8,CharOption.Numeric);
    dataDic['nid'] = getIcrcharImgpathOriginalDic(3, CharOption.Numeric);
    dataDic['stdntCount'] = getIcrcharImgpathOriginalDicForStdcount(1, CharOption.Numeric);
    dataDic['amount'] = getIcrcharImgpathOriginalDicForAmount(dataDic['stdntCount']['original'])

    return dataDic

def getData():
    dataList = []
    for index in range (1,noOfEntryInDS):
        dataList.append(createDataDic(index))
    return dataList;

for index in range(0, totalRowToCreate):
    dictionary = {"_class" : "com.progoti.kycreader.server.core.domains.DisbursementSheet"}
    dictionary['scannerId'] = getScannerId(index);
    dictionary['seq'] = getSeq(index);
    dictionary['srcFileName'] = getSrcFileName()
    dictionary['fullImg'] = getFullImg();
    dictionary['status'] = getStatus();
    dictionary['schoolCode'] = getSchoolCode(12, CharOption.Numeric);
    dictionary['data'] = getData();

    print dictionary['data'];