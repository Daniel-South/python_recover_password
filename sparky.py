"""
FILE:		sparky.py
TITLE:		Recover a weak password by matching guesses to a known hash string
AUTHOR:		Daniel R. South
DATE:		24 February 2024

DESCRIPTION:	Oops! You can't remember one of your passwords. Luckily, you have two pieces
		of information that might help you recover it.

		First, you think that the password might be based on your dog's name (Sparky).
		It might be Sparky followed by a number, possibly with a special character in between:
			Sparky33
			Spark.99

		Second, You have a hash version of the encrypted password. If you can convert likely
		combinations into hash strings, you can compare thoses hashes to the original.
		If you find a match, you will have recovered your lost password.

DISCLAIMER:	Please do not use this method for neferious purposes. It's not nice to crack other
		people's passwords, even if those passwords are weak. Everyone is entitled to privacy.
		Please be a good citizen.

		If you have a weak password, please consider making is stronger. This program
		demonstrates how easily a hacker who knows something about you can compromise
		your privacy.
"""


import hashlib


# Sparky's password converted to a hash string
known_hash_string = "f163f41d8031c6e976d7dfc0f89bb459a75cd00a1069034fb5db29d6be54ceea"


# Special characters that might be found in the password.
# The tuple inclcudes an empty string for cases where there is no special character
# between Sparky and the number.

special_chars = ('', '.', ',', '-', '_', '!')


# Generator to return a numeric string padded with leading zeros
def get_num_str(min_val, max_val, str_len):
	counter = min_val
	while counter < max_val + 1:
		str_val = str(counter).zfill(str_len)
		yield(str_val)
		counter += 1


# Try different combinations until you find one that matches the original hash string
def try_some_passwords():
	print("try_some_passwords")

	# Let's try to crack Sparky's password using two-digit numbers.
	for num_str in get_num_str(0,99,2):
		for sp_char in special_chars:
			string_to_try = "Sparky" + sp_char + num_str
			# print(string_to_try)

			# Turn the string to try into a hash
			hash_obj = hashlib.sha256()
			hash_obj.update(string_to_try.encode())
			this_hash_str = hash_obj.hexdigest()

			# Check whether the hash of this string matches the hash of your original password
			if this_hash_str == known_hash_string:
				print("The password is:", string_to_try)
				return True
	return False


# *** MAIN PROGRAM ***

print("*** Attempting to Recover Sparky's Password ***")

search_results = try_some_passwords()


if search_results == True:
	print("Congratulations!")
else:
	print("Sorry, we could not find Sparky's password.")
