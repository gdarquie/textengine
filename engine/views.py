from django.http import HttpResponse
from engine.models import Character
import random

def generateCharacter():
    character = Character()
    character.name = 'Okita'
    character = giveRiseToCharacter(character)
    return character

def giveRiseToCharacter(character):
    character.birthPlace = 'Tokyo'
    return character


def createText():
    okita = generateCharacter()
    return okita.name + ' est né à ' + okita.birthPlace + '. Il grandit '+ okita.birthPlace +'. Il est tué en 2300 par Lomma.'
 
def computeText(text):
    return 'text is computed'

def createNarrative():
    narrativeText = createText()
    computeText(narrativeText)

def createResponse():
    # rdm = random.randrange(2)
    text = createText()

    # if rdm == 0:
    #     response = 'This is the Shinsen Template from variable. First choice.'
    # else:
    #     response = 'This is the Shinsen Template from variable. Second choice.'
    
    return text

def index(request):
    response = createResponse()
    return HttpResponse(response)
