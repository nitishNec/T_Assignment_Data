import sys
import os
import random
import string

#Function to generate the random string with combination of letter, digit and special char

def randomStringwithDigitsAndSymbols(minstringLength, maxstringLength):
	mix_characters = string.ascii_letters + string.digits + string.punctuation

	return ''.join(random.choice(mix_characters) 

for i in range(minstringLength, maxstringLength))
print("Generating Random String with letters, digits and special characters ")

Random_string_generated=randomStringwithDigitsAndSymbols(1,10)

print (Random_string_generated)
