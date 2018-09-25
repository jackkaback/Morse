//
// Created by jack on 9/24/18.
//

#include<iostream>
#include<bits/stdc++.h>

int main(){

	std::map<char, std::string> morseMap = {
			{'a', "*- "},
			{'b', "-*** "},
			{'c', "-*-* "},
			{'d', "-** "},
			{'e', "* "},
			{'f', "**-* "},
			{'g', "--* "},
			{'h', "**** "},
			{'i', "** "},
			{'j', "*--- "},
			{'k', "-*- "},
			{'l', "*-** "},
			{'m', "-- "},
			{'n', "-* "},
			{'o', "--- "},
			{'p', "*--* "},
			{'q', "--*- "},
			{'r', "*-* "},
			{'s', "*** "},
			{'t', "- "},
			{'u', "**- "},
			{'v', "***- "},
			{'w', "*-- "},
			{'x', "-**- "},
			{'y', "-*-- "},
			{'z', "--** "},
			{'0', "----- "},
			{'1', "*---- "},
			{'2', "**--- "},
			{'3', "***-- "},
			{'4', "****- "},
			{'5', "***** "},
			{'6', "-**** "},
			{'7', "--*** "},
			{'8', "---** "},
			{'9', "----* "},
			{'.', "*-*-*- "},
			{'?', "**--** "},
			{' ', "\t"}
	};

	std::string input;

	while (true){
		std::cout << "Enter text to translate" << std::endl;
		std::cin >> input;

		std::transform(input.begin(), input.end(), input.begin(), ::tolower);

		if (input == "qqq"){
			break;
		}

		for(int ii = 0; ii < input.length(); ii++){
			std::cout << morseMap.at(input[ii]);
		}

		std::cout << std::endl;
	}
	return 0;
}