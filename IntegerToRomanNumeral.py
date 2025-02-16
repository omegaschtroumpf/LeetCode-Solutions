# https://leetcode.com/problems/integer-to-roman/description/

VALUE_NUMERALS = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',  90: 'XC'}
VALUE_NUMERALS |= {50: 'L', 40: 'XL', 10:'X', 9: 'IX', 5:'V', 4: 'IV', 1: 'I'}

def integer_to_roman_numeral(i):
    """
    Convert a given number to a Roman numeral.

    :param i: number to convert
    :type : integer
    :rtype: string
    """
    result = ''
    for (value) in VALUE_NUMERALS:
        how_many = i // value # Determine how many multiples of the current value are in i.
        result += how_many * VALUE_NUMERALS[value] # Append the current numeral the correct number of times.
        i -= how_many * value # Deduct the outputted value from i.
    return result
# end integer_to_roman_numeral

def roman_numeral_to_integer(s):
    """
    Convert a given Roman numeral to an integer.

    :param s: numeral to convert
    :type : string
    :rtype: int
    """
    if len(s) == 0:
        return 0
    result = 0
    search_position = 0
    for value in VALUE_NUMERALS:
        numeral = VALUE_NUMERALS[value]
        numeral_length = len(numeral)
        while (search_position < len(s)):
            # Determine if the numeral matches the current position.
            if (s.find(numeral, search_position, search_position + numeral_length) == search_position):
                # Add to the return value and advance position in the string.
                result += value
                search_position += len(numeral)
            else:
                break # The current numeral is not a match.  Continue through the list.
    return result
# end roman_numeral_to_integer

# For verification
for i in range(1,150, 17):
    numeral = integer_to_roman_numeral(i)
    print(str(i) + " " + numeral + " " + str(roman_numeral_to_integer(numeral)))
for i in range(2,3800, 177):
    numeral = integer_to_roman_numeral(i)
    print(str(i) + " " + numeral + " " + str(roman_numeral_to_integer(numeral)))