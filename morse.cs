using System;
using System.Collections.Generic;

namespace testing
{
	class Program
	{
		static void Main(string[] args)
		{
			Dictionary<char, string> map = new Dictionary<char, string>();
			
			map.Add('a', "*- ");
			map.Add('b', "-*** ");
			map.Add('c', "-*-* ");
			map.Add('d', "-** ");
			map.Add('e', "* ");
			map.Add('f', "**-* ");
			map.Add('g', "--* ");
			map.Add('h', "**** ");
			map.Add('i', "** ");
			map.Add('j', "*--- ");
			map.Add('k', "-*- ");
			map.Add('l', "*-** ");
			map.Add('m', "-- ");
			map.Add('n', "-* ");
			map.Add('o', "--- ");
			map.Add('p', "*--* ");
			map.Add('q', "--*- ");
			map.Add('r', "*-* ");
			map.Add('s', "*** ");
			map.Add('t', "- ");
			map.Add('u', "**- ");
			map.Add('v', "***- ");
			map.Add('w', "*-- ");
			map.Add('x', "-**- ");
			map.Add('y', "-*-- ");
			map.Add('z', "--** ");
			map.Add('0', "----- ");
			map.Add('1', "*---- ");
			map.Add('2', "**--- ");
			map.Add('3', "***-- ");
			map.Add('4', "****- ");
			map.Add('5', "***** ");
			map.Add('6', "-**** ");
			map.Add('7', "--*** ");
			map.Add('8', "---** ");
			map.Add('9', "----* ");
			map.Add('.', "*-*-*- ");
			map.Add('?', "**--** ");
			map.Add(' ', "\t");


			while (true)
			{
				string text;
				Console.WriteLine("Enter your Text");

				text = Console.ReadLine();
				text = text.ToLower();
				if (text.Equals("qqq"))
				{
					break;
				}

				foreach (char ii in text)
				{
					Console.Write(map[ii]);
				}
				Console.WriteLine();
			}
		}
	}
}