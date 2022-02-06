

letters = {
    "a": "1", 
    "b": "3", 
    "c": "5", 
    "d": "7",
    "e": "9", 
    "f": "11",
    "g": "13", 
    "h": "15", 
    "i": "17", 
    "j": "19",
    "k": "21", 
    "l": "23", 
    "m": "25", 
    "n": "27", 
    "o": "29", 
    "p": "31", 
    "q": "33", 
    "r": "35", 
    "s": "37", 
    "t": "39", 
    "u": "41",
    "v": "43",
    "w": "45",
    "x": "47", 
    "y": "49", 
    "z": "51",

    "A": "2", 
    "B": "4", 
    "C": "6", 
    "D": "8",
    "E": "10", 
    "F": "12",
    "G": "14", 
    "H": "16", 
    "I": "18", 
    "J": "20",
    "K": "22", 
    "L": "24", 
    "M": "26", 
    "N": "28", 
    "O": "30", 
    "P": "32", 
    "Q": "34", 
    "R": "36", 
    "S": "38", 
    "T": "40", 
    "U": "42",
    "V": "44",
    "W": "46",
    "X": "48", 
    "Y": "50", 
    "X": "52",
}

infile = open('info_security.txt','r')
read_file = infile.read()

code = "" 

for x in read_file:
    if x not in letters.keys():
        code +=x 
    else:
        y = letters[x]
        code += y 


encrypted_file = open('encrypted_file.txt','w')
encrypted_file.write(code)



        



encrypted_file.close()