while True:
    n = input()
    if n =="#":
        break
    moeum = 0
    for number in n.lower():
        if (number == "a" or number == "e" or number == "i" or number == "o" 
            or number == "u"):
            moeum += 1
    print(moeum)