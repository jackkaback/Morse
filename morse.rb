#!/usr/bin/env ruby


morseDict = {
    'a' => "*- ",
    'b' => "-*** ",
    'c' => "-*-* ",
    'd' => "-** ",
    'e' => "* ",
    'f' => "**-* ",
    'g' => "--* ",
    'h' => "**** ",
    'i' => "** ",
    'j' => "*--- ",
    'k' => "-*- ",
    'l' => "*-** ",
    'm' => "-- ",
    'n' => "-* ",
    'o' => "--- ",
    'p' => "*--* ",
    'q' => "--*- ",
    'r' => "*-* ",
    's' => "*** ",
    't' => "- ",
    'u' => "**- ",
    'v' => "***- ",
    'w' => "*-- ",
    'x' => "-**- ",
    'y' => "-*-- ",
    'z' => "--** ",
    '0' => "----- ",
    '1' => "*---- ",
    '2' => "**--- ",
    '3' => "***-- ",
    '4' => "****- ",
    '5' => "***** ",
    '6' => "-**** ",
    '7' => "--*** ",
    '8' => "---** ",
    '9' => "----* ",
    '.' => "*-*-*- ",
    '?' => "**--** ",
    ' ' => "\t"
}

while true
  puts "Enter text to translate: "
	text = gets

	temp = ""

	text.each_char { |c|
		temp << morseDict[c]
		puts c

	}

	puts temp
end