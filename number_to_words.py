# def number_to_words(number) :
#     num_dict = {0:"zero",1:"one",2:"Two",3:"Three" ,4 :"four" ,5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"Eleven" ,12 :"Twelve",13:"Thirteen"
#         ,14:"fourteen" ,15 :"fifteen" ,16 :"sixteen" ,17 :"seventeen" ,18 :"eighteen", 19 :"ninety" ,20 :"twenty",
#         30:"thirty" ,40:"fourty" ,50:"fifty",60:"sixty",70:"seventy" ,80 :"eighty" , 90:"ninty"
#         ,100:"one hundered" ,200:"two hundered" ,300:"three hundered" , 400 :"four hundered" , 500: "five hundered"
#         , 600:"six hundered" ,700:"seven hundered" ,800:"eight hundered" , 900 :"nine hundered"
#         ,1000: "Thousand", 1000000: "Million", 1000000000:"Billion"}
#     if number in num_dict:
#             return num_dict[number]         # Handle zero Case
#     if number < 100:
#             return num_dict[number // 10 * 10] + ' ' + num_dict[number % 10]
#     if number < 1000:
#         return num_dict[number // 10] + ' hundered ' + number_to_words(number % 10)
#     if number < 10000:
#             return num_dict[number // 1000] + ' hundered ' + number_to_words(number % 1000)
#     # if number < 10000:
#     #         return num_dict[number // 1000] + ' thousand ' + number_to_words(number % 1000)
#
#
#     if number < 100000:
#             return num_dict[number // 10000] + ' thousand '+ number_to_words(number % 10000)
#     if number < 10000000:
#             return num_dict[number // 100000] + ' thousand ' + number_to_words(number % 100000)
#
#     if number < 1000000:  # 1234567
#         return num_dict[number//100000] + ' Million '+ number_to_words(number % 100000)
#     if number < 10000000:
#         return num_dict[number // 1000000] + ' Million ' + number_to_words(number % 1000000)
#     if number <= 1000000000:
#         return num_dict[number // 10000000] + ' Billion ' + number_to_words(number % 10000000)
#     if number < 10000000000:
#         return num_dict[number // 100000000] + 'Billion' + number_to_words(number % 100000000)
#
#
# number = int(input("Enter the number"))
# print(number_to_words(number))
#
#

#  2
# def numberToWords(number):
#     num_dict = {
#         0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
#         10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
#         17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
#         60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
#         100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
#         600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred",
#         1000: "thousand", 1000000: "million", 1000000000: "billion"
#     }
#
#     if number in num_dict:
#         return num_dict[number]
#     elif number < 100:
#         return num_dict[number // 10 * 10] + ' ' + num_dict[number % 10]
#     elif number < 1000:
#         return num_dict[number // 100] + ' hundred '+ numberToWords(number % 100)
#     elif number < 1000000:
#         return numberToWords(number // 1000) + ' thousand ' + numberToWords(number % 1000)
#     elif number < 1000000000:
#         return numberToWords(number // 1000000) + ' million ' + numberToWords(number % 1000000)
#     else:
#         return numberToWords(number // 1000000000) + ' billion ' + numberToWords(number % 1000000000)
#
# number = int(input("Enter the number: "))
# print(numberToWords(number))
#


# 3 [ Better Conversion ]
def numberToWords(number) :
    num_dict ={0: "zero", 1: "one", 2:"two", 3: "three", 4:"four", 5:"five", 6: "six", 7: "seven", 8: "eight", 9:"nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
        100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
        600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred",
        1000: "thousand", 1000000: "million", 1000000000: "billion" }

    if number == 0:
        return "Zero"  # Zero Case .
    elif number < 20:
        return num_dict[number]
    elif number < 100:
        return num_dict[number // 10 * 10] + ('' if number % 10 == 0 else ' ' + num_dict[number % 10])
    elif number < 1000:
        return num_dict[number // 100] + ' Hundred' + ('' if number % 100 == 0 else ' ' +
                                                                                    numberToWords(number % 100))
    elif number < 1000000:
        return numberToWords(number // 1000) + ' Thousand' + ('' if number % 1000 == 0 else ' ' +
                                                                                                 numberToWords(
                                                                                                     number % 1000))
    elif number < 1000000000:
        return numberToWords(number // 1000000) + ' Million' + (
            '' if number % 1000000 == 0 else ' ' + numberToWords(number % 1000000))
    else:
        return numberToWords(number // 1000000000) + ' Billion' + ('' if number % 1000000000 == 0
                                                                        else ' ' + numberToWords(
            number % 1000000000))


number = int(input("Enter the Number"))
print(numberToWords(number))




