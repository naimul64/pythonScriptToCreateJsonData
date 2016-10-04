import random

def createNID():
    return "12345678901234567"

def getRandomConfidence():
    return random.randrange(50, 100)

confidence = getRandomConfidence()
print confidence;