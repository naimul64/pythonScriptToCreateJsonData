import random

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
    return str(index%noOfScanBySingleScanner + 1);

def getSrcFileName():
    return "rotate.pdf";

def getFullImg():
    return "rotate.pdf";

def getimgPath():
    return "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Einstein_Szilard_p1.jpg/220px-Einstein_Szilard_p1.jpg"

def getStatus():
    return "PROCESSED"


for index in range(1, 1000):
    dictionary = {"_class" : "com.progoti.kycreader.server.core.domains.DisbursementSheet"}
    dictionary['scannerId'] = getScannerId(index);
    dictionary['seq'] = getSeq(index);
    dictionary['srcFileName'] = getSrcFileName()
    dictionary['fullImg'] = getFullImg();
    dictionary['status'] = getStatus()


    print dictionary;
