def anagram_number(number):
    return str(number) == str(number)[::-1]

def roman_to_int(s):
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    roman = s.strip().upper()
    result = 0
    i = 0
    while i < len(roman):
        value = romans[roman[i]]
        if i < len(roman) - 1:
            next = romans[roman[i + 1]]
            if value < next:
                result += next - value
                i += 1
            else:
                result += value
        else:
            result += value
        i += 1
    return result