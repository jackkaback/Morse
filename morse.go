package main

import (
	"fmt"
	"strings"
)

func main() {

	//think of bytes as char
	var morseDict map[byte]string
	morseDict = make(map[byte]string)

	morseDict['a'] = "*- "
	morseDict['b'] = "-*** "
	morseDict['c'] = "-*-* "
	morseDict['d'] = "-** "
	morseDict['e'] = "* "
	morseDict['f'] = "**-* "
	morseDict['g'] = "--* "
	morseDict['h'] = "**** "
	morseDict['i'] = "** "
	morseDict['j'] = "*--- "
	morseDict['k'] = "-*- "
	morseDict['l'] = "*-** "
	morseDict['m'] = "-- "
	morseDict['n'] = "-* "
	morseDict['o'] = "--- "
	morseDict['p'] = "*--* "
	morseDict['q'] = "--*- "
	morseDict['r'] = "*-* "
	morseDict['s'] = "*** "
	morseDict['t'] = "- "
	morseDict['u'] = "**- "
	morseDict['v'] = "***- "
	morseDict['w'] = "*-- "
	morseDict['x'] = "-**- "
	morseDict['y'] = "-*-- "
	morseDict['z'] = "--** "
	morseDict['0'] = "----- "
	morseDict['1'] = "*---- "
	morseDict['2'] = "**--- "
	morseDict['3'] = "***-- "
	morseDict['4'] = "****- "
	morseDict['5'] = "***** "
	morseDict['6'] = "-**** "
	morseDict['7'] = "--*** "
	morseDict['8'] = "---** "
	morseDict['9'] = "----* "
	morseDict['.'] = "*-*-*- "
	morseDict['?'] = "**--** "
	morseDict[' '] = "\t"

	var words string
	for {
		_, _ = fmt.Scanf("%s", &words)

		//make everything lower case to avoid issues
		words = strings.ToLower(words)

		for i := 0; i < len(words); i++ {
			fmt.Printf("%s", morseDict[words[i]])
		}
		fmt.Println()
	}

}
