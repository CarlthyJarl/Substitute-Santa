def skapa():
    fil_n = input("Skriv namnet på filen: ")
    barn_n = input("Skriv namnet på barnet: ")
    with open(fil_n, "w", encoding="utf8") as fil:
        fil.write(barn_n + "\n"*2)
        pres_antal = int(input("Skriv in antalet önskningar: "))
        for i in range(1, pres_antal+1):
            fil.write(input(F"Skriv föremål numer {i}: ")+"\n")

def läsa():
    fil_n = input("Vad heter filen du vill läsa upp? ")
    with open(fil_n, "r", encoding="utf8") as fil:
        lines = fil.readlines()
        namn = lines[0]
        print(F"{namn}ville ha:")
        for i in range(2, len(lines)):
            print(lines[i], end="")




def meny():
    tr = True
    print("Welcome to program...")
    while tr:
        print("Tryck 1 för att göra en önskelista tryck 2 för att läsa upp den och 3 för att avsluta programet")
        val = int(input("   - "))
        if val == 1:
            skapa()
        elif val == 2:
            läsa()
        elif val == 3:
            print("programet har avslutats...")
            tr = False
        else:
            pass

def main():
    meny()

if __name__ == "__main__":
    main()