def addTwo(x,y):return x+y
def addTwo(x,y):return x-y

def hangmanAscii (input):
  HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|\  |
  /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
  /|\  |
  / \  |
        |
  =========''']
  return HANGMANPICS[input]