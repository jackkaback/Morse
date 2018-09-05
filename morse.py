#!/usr/bin/python2.7


def translations(char):

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

    return morseDict.get(char)


#print translations("c")

while True:
    string = raw_input()
    string = string.lower()

    if string == "qqq":
        break

    s = ""

    for c in string:
        s += str(translations(c))

    print s
