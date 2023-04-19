import random

print("اهلا بيك في صانع الباسورد العشوائي")

strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['?', '!', ':', '*', '$', '@', '+', '-', '&', '_', '/', '\\', '∆', '¶', '×', '÷', 'π', '√', '•', '|', '`', '~', '£', '¢', '€', '¥', '^', '°', '=', '\\', '%', '©', '®', '™', '✓', '#']

letter = int(input("عاوز الباسورد من كام حرف ؟ "))

num = int(input("عايز الباسورد من كام رقم ؟ "))

symbol = int(input("عاوز الرقم من كام علامه مميزه ؟ "))

captial_or_small = input("عايز الحروف كبيرة ولا صغيرة ؟ ")

if captial_or_small == 'كبيرة':
	strings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	
else:
	None
	
random_letter = random.choices(strings, k=letter)


random_num = random.choices(nums, k=num)

random_symbol = random.choices(symbols, k=symbol)

random_password = random_letter +  random_num + random_symbol
random.shuffle(random_password)

print('' .join(random_password))
