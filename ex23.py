#!/usr/bin/python3.6

# Exercise 23: Strings, Bytes, and Characters Encoding

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline()
	
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<====>", cooked_string)

print("Let's open languages.txt file now\n")

languages = open("languages.txt", encoding="utf-8")

print("We are now under languages line")

main(languages, input_encoding, error)
