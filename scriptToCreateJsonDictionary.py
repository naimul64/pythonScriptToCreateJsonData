import random

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

dictionary = ["_class" : "com.progoti.kycreader.server.core.domains.DisbursementSheet"]