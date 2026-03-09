import re

number_words = {
"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,
"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,
"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,
"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,
"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,
"eighty":80,"ninety":90
}

operations = {
"plus":"+",
"add":"+",
"minus":"-",
"subtract":"-",
"times":"*",
"multiplied by":"*",
"multiply":"*",
"into":"*",
"divided by":"/",
"divide":"/",
"over":"/"
}


def convert_words_to_numbers(text):

    for word, number in number_words.items():
        text = text.replace(word, str(number))

    return text


def convert_words_to_symbols(text):

    for word, symbol in operations.items():
        text = text.replace(word, symbol)

    return text


def calculate_expression(text):

    text = text.lower()

    text = convert_words_to_numbers(text)

    text = convert_words_to_symbols(text)

    text = re.sub(r"[^0-9+\-*/(). ]", "", text)

    try:
        result = eval(text)
        return result
    except Exception:
        return None