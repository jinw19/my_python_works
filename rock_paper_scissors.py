import random

print(("-" * 30) + "\ntas, kagit, makas Oyununa hos geldin")

senin_skorun, pc_skoru = 0,0

while True:
    print("1-) tas, 2-) kagit, 3-) makas")
    senin_secimin = input("secimini gir:")
    pc_secimi = random.choice(["1","2","3"])

    if senin_secimin == "1":

        if pc_secimi == "1":
            print("ikinizde tas sectiniz berabere")
        
        if pc_secimi == "2":
            print(("pc kagit secti seni hakladi"))
            pc_skoru += 1
        
        if pc_secimi == "3":
            print("pc makasi secti sen pcyi ezdin")
            senin_skorun +=1

    if senin_secimin == "2":

        if pc_secimi == "1":
            print("pc tas secti sen pcyi hakladin")
            senin_skorun += 1
        
        if pc_secimi == "2":
            print("ikinizde kagit sectiniz berabere")

        if pc_secimi == "3":
            print("pc makas secti seni bicti")
            pc_skoru += 1

    if senin_secimin == "3":

        if pc_secimi == "1":
            print("pc tas secti pc seni ezdi")
            pc_skoru += 1
        
        if pc_secimi == "2":
            print("pc kagit secti sen pcyi bictin")
            senin_skorun += 1
        
        if pc_secimi == "3":
            print("ikinizde makas sectiniz berabere")

    print("senin skorun {}, pc skoru {}".format(senin_skorun,pc_skoru))
   
    
    

