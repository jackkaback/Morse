use std::collections::HashMap;

fn main() {
    let mut morseDict = HashMap::new();

    morseDict.insert("a".to_string(), "*- ".to_string());
    morseDict.insert("b".to_string(), "-*** ".to_string());
    morseDict.insert("c".to_string(), "-*-* ".to_string());
    morseDict.insert("d".to_string(), "-** ".to_string());
    morseDict.insert("e".to_string(), "* ".to_string());
    morseDict.insert("f".to_string(), "**-* ".to_string());
    morseDict.insert("g".to_string(), "--* ".to_string());
    morseDict.insert("h".to_string(), "**** ".to_string());
    morseDict.insert("i".to_string(), "** ".to_string());
    morseDict.insert("j".to_string(), "*--- ".to_string());
    morseDict.insert("k".to_string(), "-*- ".to_string());
    morseDict.insert("l".to_string(), "*-** ".to_string());
    morseDict.insert("m".to_string(), "-- ".to_string());
    morseDict.insert("n".to_string(), "-* ".to_string());
    morseDict.insert("o".to_string(), "--- ".to_string());
    morseDict.insert("p".to_string(), "*--* ".to_string());
    morseDict.insert("q".to_string(), "--*- ".to_string());
    morseDict.insert("r".to_string(), "*-* ".to_string());
    morseDict.insert("s".to_string(), "*** ".to_string());
    morseDict.insert("t".to_string(), "- ".to_string());
    morseDict.insert("u".to_string(), "**- ".to_string());
    morseDict.insert("v".to_string(), "***- ".to_string());
    morseDict.insert("w".to_string(), "*-- ".to_string());
    morseDict.insert("x".to_string(), "-**- ".to_string());
    morseDict.insert("y".to_string(), "-*-- ".to_string());
    morseDict.insert("z".to_string(), "--** ".to_string());
    morseDict.insert("0".to_string(), "----- ".to_string());
    morseDict.insert("1".to_string(), "*---- ".to_string());
    morseDict.insert("2".to_string(), "**--- ".to_string());
    morseDict.insert("3".to_string(), "***-- ".to_string());
    morseDict.insert("4".to_string(), "****- ".to_string());
    morseDict.insert("5".to_string(), "***** ".to_string());
    morseDict.insert("6".to_string(), "-**** ".to_string());
    morseDict.insert("7".to_string(), "--*** ".to_string());
    morseDict.insert("8".to_string(), "---** ".to_string());
    morseDict.insert("9".to_string(), "----* ".to_string());
    morseDict.insert(".".to_string(), "*-*-*- ".to_string());
    morseDict.insert("?".to_string(), "**--** ".to_string());
    morseDict.insert(" ".to_string(), "\t".to_string());


    while true{
        let mut input = String::new();

        match io::stdin().read_line(&mut input) {
            Ok(n) => {
                println!("{} bytes read", n);
                println!("{}", input);
            }
            Err(error) => println!("error: {}", error),
        }

        for c in input.chars() {


        }
    }
}