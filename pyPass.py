import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = [ 
  "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "<", ">", ",", ".", "?" , "/", "`", "~",
  '"', '\'', "€", "£", "¥", "§", "©", "®", "™", "µ", "…", "x", "÷", "∞", "β", "∑", "π", "√", "∫", "∂", "∆", "Ω", "Ξ", "Ψ",
  "—", "…", "«", "»", "♥", "♠", "♣", "♦"
]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

password_length = int(input("Enter your password length: "))

password = []

for _ in range(password_length):
    if random.randint(0, 1) == 0:
        password.append(random.choice(letters))
    elif random.randint(0, 1) == 0:
        password.append(random.choice(symbols))
    else:
        password.append(random.choice(numbers))

random.shuffle(password)

password_string = ''.join(password)

print(password_string)