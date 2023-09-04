#my_str = "shubham pundhir"
#print(my_str.isalnum())
#print(my_str.isalpha())
#print(my_str.isdigit())
#print(my_str.istitle())
#print(my_str.isupper())
#print(my_str.islower())
#print(my_str.isspace())
#print(my_str.endswith('d'))
#print(my_str.startswith('H'))


import random

# Generates a random number between
# a given positive range
r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))

# Generates a random number between
# two given negative range
r2 = random.randint(-10, -1)
print("Random number between -10 and -1 is % d" % (r2))

# Generates a random number between
# a positive and a negative range
r3 = random.randint(-5, 5)
print("Random number between -5 and 5 is % d" % (r3))