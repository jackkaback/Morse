#!/usr/bin/python2.7


def translations(char):

    morseDict = {
        "a": "*-",
        "b": "-***",
        "c": "-*-*",
        "d": "-**",
        "e": "*",
        "f": "**-*",
        "g": "--*",
        "h": "****",
        "i": "**",
        "j": "*---",
        "k": "-*-",
        "l": "*-**",
        "m": "--",
        "n": "-*",
        "o": "---",
        "p": "*--*",
        "q": "--*-",
        "r": "*-*",
        "s": "***",
        "t": "-",
        "u": "**-",
        "v": "***-",
        "w": "*--",
        "x": "-**-",
        "y": "-*--",
        "z": "--**"
    }

    print len(morseDict)


translations("c")

while True:
    string = raw_input()
    print "Hello world"
