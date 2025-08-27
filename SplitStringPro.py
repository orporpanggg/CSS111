my_sentence = "It's suggested to walk, study, and sleep everyday"
stop = {" ", ",", ";", ":"}
lower_sentence = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz"
)

lower_mysentence = my_sentence.translate(lower_sentence)

oneword = ""
words = []
for char in lower_mysentence:
    if char not in stop:
        oneword += char
    else:
        if oneword != "":
            words.append(oneword)
        oneword = ""
        
words.append(oneword)
        
for oneword in words:
    print(oneword)
    
print(len(words))