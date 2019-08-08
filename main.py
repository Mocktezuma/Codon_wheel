stop = ["uaa", "uag", "uga"]
codon = ""


def printResult(result):  # define a function for printing the result based on a variable
    print(f"Your codon is {result}.")


def codoncheck(codonlist):
    if codon in stop:
        printResult("stop")
    elif codonlist[0] == "g":
        if codonlist[1] == "g":
            printResult("Glycine")
        elif codonlist[1] == "u":
            printResult("Valine")
        elif codonlist[1] == "c":
            printResult("Alanine")
        else:
            if codonlist[2] == "a" or codonlist[2] == "g":
                printResult("Glutamic acid")
            else:
                printResult("Aspartic acid")
    elif codonlist[0] == "u":
        if codonlist[1] == "c":
            printResult("Serine")
        elif codonlist[1] == "a":
            printResult("Tyrosine")
        elif codonlist[1] == "u":
            if codonlist[2] == "a" or codonlist[2] == "g":
                printResult("Phenylalanine")
            else:
                printResult("Leucine")
        else:
            if codonlist[2] == "u" or codonlist[2] == "c":
                printResult("Cysteine")
            else:
                printResult("Tryptophan")
    elif codonlist[0] == "a":
        if codonlist[1] == "c":
            printResult("Threonine")
        elif codonlist[1] == "g":
            if codonlist[2] == "g" or codonlist[2] == "a":
                printResult("Arginine")
            else:
                printResult("Serine")
        elif codonlist[1] == "a":
            if codonlist[2] == "g" or codonlist[2] == "a":
                printResult("Lysine")
            else:
                printResult("Asparagine")
        else:
            if codonlist[2] == "g":
                printResult("Methionine")
            else:
                printResult("Isolleucine")
    elif codonlist[0] == "c":
        if codonlist[1] == "u":
            printResult("Leucine")
        elif codonlist[1] == "c":
            printResult("Proline")
        elif codonlist[1] == "g":
            printResult("Arginine")
        else:
            if codonlist[2] == "u" or codonlist[2] == "c":
                printResult("Histidine")
            else:
                printResult("Glutamine")
    else:
        print("Error: please enter a valid codon")


while codon != "exit":  # loops until the codon has 3 characters
    print("Please enter a codon with 3 letters: ")
    codon = input("> ")
    codonlist = list(codon)  # turn codon into a list
    codoncheck(codonlist)
