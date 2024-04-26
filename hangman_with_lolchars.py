import random

pics = ["""
    +---+
    |   | 
        | 
        | 
        | 
        | 
========= """, """

   +---+
   |   | 
   O   | 
       | 
       | 
       | 
========= ""","""

   +---+
   |   | 
   O   | 
   |   | 
       | 
       | 
========= """, """

   +---+
   |   | 
   O   | 
  /|   | 
       | 
       | 
========= """, """

   +---+
   |   | 
   O   | 
  /|\  | 
       | 
       | 
========= """, """

   +---+
   |   | 
   O   | 
  /|\  | 
  /    | 
       | 
========= """, """

   +---+
   |   | 
   O   | 
  /|\  | 
  / \  | 
       | 
========= """]

while True:
    print(("-" * 30) + "\nHangman Game\n" + ("-" * 30))

    words = random.choice(["akali", "zed", "katarina", "kayn", "urgot", "garen", "aatrox", "rengar", "gwen", "talon", "kalista", "darius", "lissandra"])
    step = 0
    letters = []

    while True:
        print(pics[step])

        for i, char in enumerate(words):
            print(char if i in letters else "_"),
        
        answer = input("\nAnswer: ")
        
        if answer == words:
            print("YOU WIN!!\n")
            break
        else:
            while True:
                rand = random.randint(0, len(words))
                if not rand in letters:
                    letters.append(rand)
                    break
            step += 1
        
        if step>= len(pics):
            print("YOU LOSE!!\n\n")
            break
    if not "y" == input("PLAY AGAİN ? (Y/N)"):
        break
