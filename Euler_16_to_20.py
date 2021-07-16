# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 10:18:15 2021

@author: 82108
"""

"""
No.16 [Power digit sum]

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def power_digit_sum_2(square) :
    result = 0
    num = 2 ** square
    str_num = str(num)
    for s in str_num :
        result += int(s)
    return result

answer = power_digit_sum_2(1000)
print(answer) # 1366

'''
[The answer]
1366
'''











"""
No.17 [Number letter counts]

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

num_dict = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
            18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'senventy',
            80:'eighty', 90:'ninety', 100:'onehundredand', 200:'twohundredand', 300:'threehundredand', 400:'fourhundredand',
            500:'fivehundredand', 600:'sixhundredand', 700:'sevenhundredand', 800:'eighthundredand', 900:'ninehundredand',
            1000:'onethousand'}

def num_trans_str(number) :
    word_list = []
    for i in range(1, number+1) : # 1 ~ 19
        if i < 20 :
            word = num_dict[i]
            word_list.append(word)
        elif i >= 20 and i < 100 : # 20 ~ 99
            if i % 10 == 0 :
                word = num_dict[i]
                word_list.append(word)
            else : 
                tenth = i - (i % 10)
                oneth = (i % 10)
                word = num_dict[tenth] + num_dict[oneth]
                word_list.append(word)
        elif i >= 100 and i < 1000 : # 100 ~ 999
            if i % 100 == 0 :
                word = num_dict[i]
                word_list.append(word)
            elif i % 10 == 0 :
                hundredth = i - (i % 100)
                tenth = i % 100
                word = num_dict[hundredth] + num_dict[tenth]
                word_list.append(word)
            elif i % 10 != 0 :
                hundredth = i - (i % 100)
                tenth = (i % 100) - (i % 10)
                oneth = i % 10
                word = num_dict[hundredth] + num_dict[tenth] + num_dict[oneth]
                word_list.append(word)
        elif i == 1000 : # 1000
            word = num_dict[i]
            word_list.append(word)
    return word_list
                

final_word_list = num_trans_str(1000) 
print(final_word_list)
len(final_word_list) # 1000

cnt = 0
for word in final_word_list :
    cnt += len(word)

print(cnt) # 21215










"""
No.18 [Maximum path sum I]

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, 
it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
"""

str_num = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

# First Step : Preprocessing
import re

num_list = re.findall("[0-9]{2}", str_num)  
print(num_list)
'''
['75', '95', '64', '17', '47', '82', '18', '35', '87', '10', '20', '04', '82', 
 '47', '65', '19', '01', '23', '75', '03', '34', '88', '02', '77', '73', '07', 
 '63', '67', '99', '65', '04', '28', '06', '16', '70', '92', '41', '41', '26', 
 '56', '83', '40', '80', '70', '33', '41', '48', '72', '33', '47', '32', '37', 
 '16', '94', '29', '53', '71', '44', '65', '25', '43', '91', '52', '97', '51', 
 '14', '70', '11', '33', '28', '77', '73', '17', '78', '39', '68', '17', '57', 
 '91', '71', '52', '38', '17', '14', '91', '43', '58', '50', '27', '29', '48', 
 '63', '66', '04', '68', '89', '53', '67', '30', '73', '16', '69', '87', '40', 
 '31', '04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53', 
 '60', '04', '23']
'''
len(num_list) # 120

# Second Step : Solve

dup_list = []
answer = 0
cnt1 = 0
cnt2 = 1

# [0:1] -> [1:3] -> [3:7] -> [7:11]
# 0, 1, 3, 7
# 1, 3, 7, 11

for i in range(1, 16) :
    num = num_list[cnt1:cnt2]
    dup_list.append(num)
    cnt1 = cnt2
    cnt2 += (i + 1)

print(dup_list)
'''
[['75'], 
 ['95', '64'], 
 ['17', '47', '82'], 
 ['18', '35', '87', '10'], 
 ['20', '04', '82', '47', '65'], 
 ['19', '01', '23', '75', '03', '34'], 
 ['88', '02', '77', '73', '07', '63', '67'], 
 ['99', '65', '04', '28', '06', '16', '70', '92'], 
 ['41', '41', '26', '56', '83', '40', '80', '70', '33'], 
 ['41', '48', '72', '33', '47', '32', '37', '16', '94', '29'], 
 ['53', '71', '44', '65', '25', '43', '91', '52', '97', '51', '14'], 
 ['70', '11', '33', '28', '77', '73', '17', '78', '39', '68', '17', '57'], 
 ['91', '71', '52', '38', '17', '14', '91', '43', '58', '50', '27', '29', '48'], 
 ['63', '66', '04', '68', '89', '53', '67', '30', '73', '16', '69', '87', '40', '31'], 
 ['04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53', '60', '04', '23']]
'''
'''
[                                           ['75'],                                               -> 75
                                         ['95', '64'],                                            -> 95
                                      ['17', '47', '82'],                                         -> 47
                                   ['18', '35', '87', '10'],                                      -> 87
                                ['20', '04', '82', '47', '65'],                                   -> 82
                             ['19', '01', '23', '75', '03', '34'],                                -> 75
                          ['88', '02', '77', '73', '07', '63', '67'],                             -> 73
                       ['99', '65', '04', '28', '06', '16', '70', '92'],                          -> 28
                    ['41', '41', '26', '56', '83', '40', '80', '70', '33'],                       -> 83
                 ['41', '48', '72', '33', '47', '32', '37', '16', '94', '29'],                    -> 47
              ['53', '71', '44', '65', '25', '43', '91', '52', '97', '51', '14'],                 -> 43
           ['70', '11', '33', '28', '77', '73', '17', '78', '39', '68', '17', '57'],              -> 73
        ['91', '71', '52', '38', '17', '14', '91', '43', '58', '50', '27', '29', '48'],           -> 91
     ['63', '66', '04', '68', '89', '53', '67', '30', '73', '16', '69', '87', '40', '31'],        -> 67
 ['04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53', '60', '04', '23']]      -> 98
'''


cnt = 0
i1 = 0
i2 = 1
num_list = []

while cnt < 15 :
    if cnt == 0 :
        num = max(dup_list[cnt])
        num_list.append(num)
        cnt += 1
    elif cnt == 1 :
        num = max([dup_list[cnt][i1], dup_list[cnt][i2]])
        num_list.append(num)
        if num == dup_list[cnt][i2]:
            i1 += 1
            i2 += 1
            cnt += 1
        else :
            cnt += 1
    else :
        num = max([dup_list[cnt][i1], dup_list[cnt][i2]])
        num_list.append(num)
        if num == dup_list[cnt][i2]:
            i1 += 1
            i2 += 1
            cnt += 1
        else :
            cnt += 1

print(num_list)
# ['75', '95', '47', '87', '82', '75', '73', '28', '83', '47', '43', '73', '91', '67', '98']


answer = 0

for n in num_list :
    answer += int(n)

print(answer) # 1064

'''
[The answer]
1064
'''










"""
No.19 [Counting Sundays]

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import calendar

def counting_days(start, end) :
    count = {}
    for i in range(start, end+1) :
        for j in range(1, 13) :
            day = calendar.weekday(i, j, 1)
            count[day] = count.get(day, 0) + 1
    return count

'''
0 : 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
'''
        
answer = counting_days(1901, 2000)[6]
print(answer) # 171

'''
[The answer]
171
'''










"""
No.20 [Factorial digit sum]

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math

def find_factorial_digit_sum(number) :
    result = 0
    num = math.factorial(number)
    str_num = str(num)
    for s in str_num : 
        result += int(s)
    return result

test = find_factorial_digit_sum(10)
print(test) # 27

answer = find_factorial_digit_sum(100)
print(answer) # 648

'''
[The answer]
648
'''







