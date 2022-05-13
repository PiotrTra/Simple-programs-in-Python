lyrics = "JESLI BEDZIE TRZEBA"


alfabet = {"A":0, "Ą": 0, "B": 0, "C": 0, "Ć": 0, "D": 0,
           "E": 0, "Ę": 0, "F": 0, "G": 0, "H": 0, "I": 0,
           "J": 0, "K": 0,"L":0,"Ł": 0, "M": 0, "N": 0, "Ń":0, "P":0,"T": 0,
           "U": 0, "W": 0, "Y": 0, "Z": 0, "Ż": 0, "Ź": 0}



for w in range(len(lyrics)):
    if lyrics[w] in alfabet:
        val = alfabet[lyrics[w]]
        val += 1
        update = {lyrics[w]:val}
        alfabet.update(update)
print(alfabet)



