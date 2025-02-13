class RomanNumeral:
    # Class level variable mapping numeric values to roman numeral strings
    ValueNumerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',  90: 'XC'}
    ValueNumerals |= {50: 'L', 40: 'XL', 10:'X', 9: 'IX', 5:'V', 4: 'IV', 1: 'I'}
    
    # given an integer i, return a string containing the Roman numeral equivalent
    def integerToRomanNumeral(i):
        result = ''
        for (value) in RomanNumeral.ValueNumerals:
            mult = i // value # determine how many multiples of the current value are in i
            result += mult * RomanNumeral.ValueNumerals[value] # append mult copies of the current numeral
            i -= mult * value # deduct the outputted value from i
        return result

    # given a Roman numeral string, return the integer value
    def romanNumeralToInteger(s):
        if len(s) == 0:
            return 0
        result = 0
        searchPos = 0
        for value in RomanNumeral.ValueNumerals:
            currentNumeral = RomanNumeral.ValueNumerals[value]
            curNumLen = len(currentNumeral)
            while (searchPos < len(s)):
                # if CurrentNumeral is a match at the current position in the string,
                # add to the return value and advance in the string
                if (s.find(currentNumeral, searchPos, searchPos + curNumLen) == searchPos):
                    result += value
                    searchPos += len(currentNumeral)
                else:
                    break
        return result

# For verification
# print Roman Numerals from 1 to 150, incrementing by 11
#for i in range(1,150, 11):
#    print(RomanNumeral.integerToRomanNumeral(i))
# print Roman Numerals from 1 to 3000 incrementing by 131
#for i in range(1,3800, 131):
#    print(RomanNumeral.integerToRomanNumeral(i))
for i in range(1,150, 11):
    t = (i == RomanNumeral.romanNumeralToInteger(RomanNumeral.integerToRomanNumeral(i)))
    print(str(i) + " " + str(t))
#print(RomanNumeral.romanNumeralToInteger("MMCDXXXVI"))