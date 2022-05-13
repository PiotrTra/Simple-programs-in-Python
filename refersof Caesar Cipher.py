alfabet = {"A": "C", "Ą": "Ć", "B": "D", "C": "E", "Ć": "Ę", "D": "F",
           "E": "G", "Ę": "H", "F": "I", "G": "J", "H": "K", "I": "L",
           "J": "Ł", "K": "M","L":"N","Ł": "Ń", "M": "O", "N": "Ó", "Ń": "P", "O": "R",
           "Ó": "S", "P": "Ś", "R": "T", "S": "U", "Ś": "W", "T": "Y",
           "U": "Z", "W": "Ż", "Y": "Ź", "Z": "A", "Ż": "B", "Ź": "Q"}

cezared= ""
tekst = "CCCCCDDDDECCC"

for letters in tekst:
    for key,value in alfabet.items():
        if letters in value:
            cezared += key

print(cezared)