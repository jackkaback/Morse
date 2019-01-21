#!/usr/bin/python2.7

from __future__ import print_function
from six.moves import input

while True:

	morseDict = {
		"a": "*- ",
		"b": "-*** ",
		"c": "-*-* ",
		"d": "-** ",
		"e": "* ",
		"f": "**-* ",
		"g": "--* ",
		"h": "**** ",
		"i": "** ",
		"j": "*--- ",
		"k": "-*- ",
		"l": "*-** ",
		"m": "-- ",
		"n": "-* ",
		"o": "--- ",
		"p": "*--* ",
		"q": "--*- ",
		"r": "*-* ",
		"s": "*** ",
		"t": "- ",
		"u": "**- ",
		"v": "***- ",
		"w": "*-- ",
		"x": "-**- ",
		"y": "-*-- ",
		"z": "--** ",
		"0": "----- ",
		"1": "*---- ",
		"2": "**--- ",
		"3": "***-- ",
		"4": "****- ",
		"5": "***** ",
		"6": "-**** ",
		"7": "--*** ",
		"8": "---** ",
		"9": "----* ",
		".": "*-*-*- ",
		"?": "**--** ",
		" ": "\t"
	}

	print("Enter text to translate")
	string = input()
	string = string.lower()

	if string == "qqq":
		break

	s = ""

	for c in string:
		s += str(morseDict.get(c))

	print(s)
