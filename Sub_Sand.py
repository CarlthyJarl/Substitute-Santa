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
        namn = lines[0].rstrip("\n")
        print(F"{namn} ville ha:")
        for i in range(2, len(lines)):
            print(lines[i], end="")

def naughtylist():
    fil_n = "bad kids"
    with open(fil_n, "r", encoding="utf8") as fil:
        lines = fil.readlines()
        print("De stygga barnen är:")
        for i in range(len(lines)):
            print(lines[i], end="")
    with open(fil_n, "a", encoding="utf8") as fil:
        barn_antal = int(input("Hur många barn vill du lägga till: "))
        if barn_antal == 0:
            print("Ait...")
        else:
            for i in range(1, barn_antal+1):
                fil.write(input(F"Skriv namnet på barn {i}: ")+"\n")

def läsa_naughtylis():
    fil_n = "bad kids"
    with open(fil_n, "r", encoding="utf8") as fil:
        lines = fil.readlines()
        print("De stygga barnen är:")
        for i in range(len(lines)):
            print(lines[i], end="")

def main():
    tr = True
    print("Welcome to le program...")
    while tr:
        print("Tryck 1 för att göra en önskelista, tryck 2 för att läsa upp den, 3 för att lägga till i naughty list,")
        print("4 för att läsa den och 5 för att avsluta programet")
        val = int(input("   - "))
        if val == 1:
            skapa()
        elif val == 2:
            läsa()
        elif val == 3:
            naughtylist()
        elif val == 4:
            läsa_naughtylis()
        elif val == 5:
            print("programet har avslutats...")
            tr = False
        else:
            print("...")

if __name__ == "__main__":
    main()