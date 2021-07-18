# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 11:58:28 2021

@author: 82108
"""

"""
No.21 [Amicable numbers]

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def find_amicable_numbers(number) :
    amicable_list = []
    div_dic = {}
    for i in range(2, number+1) :
        div_list = []
        div_sum = 0
        for j in range(1, i) :
            if i % j == 0 :
                div_list.append(j)
        for div in div_list :
            div_sum += div
        div_dic[i] = div_sum
    for k in range(2, len(div_dic)+2) :
        if div_dic[k] in div_dic.keys() and div_dic[div_dic[k]] == k:
            if k != div_dic[k] :
                amicable_list.append([k, div_dic[k]])
    return amicable_list


test = find_amicable_numbers(300)
print(test) # [[220, 284], [284, 220]]

answer = find_amicable_numbers(10000)
print(answer) 
# [[220, 284], [284, 220], [1184, 1210], [1210, 1184], [2620, 2924], [2924, 2620], 
# [5020, 5564], [5564, 5020], [6232, 6368], [6368, 6232]]

'''
[The answer]
[[220, 284], [284, 220], [1184, 1210], [1210, 1184], [2620, 2924], 
 [2924, 2620], [5020, 5564], [5564, 5020], [6232, 6368], [6368, 6232]]
=> "220 - 284" | "1184 - 1210" | "2620 - 2924" | "5020 - 5564" | "6232 - 6386"
'''










"""
No.22 [Names scores]

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import re


with open("name.txt", mode ='r', encoding = "utf-8") as f :
    data = f.read()
    
type(data) # str

# str -> list
pre_data = data.split(",")
type(pre_data) # list

final_data = []
for s in pre_data :
    st = re.findall("[A-Z]+", s)
    final_data.extend(st)

print(final_data)
# ['MARY', 'PATRICIA', 'LINDA', 'BARBARA', 'ELIZABETH', 'JENNIFER', 'MARIA', 'SUSAN', ...
# 'LYNWOOD', 'JERE', 'HAI', 'ELDEN', 'DORSEY', 'DARELL', 'BRODERICK', 'ALONSO']

'''
ASCII CODE - Alphabet

65 - A
66 - B
67 - C
   .
   .
   .
88 - X
89 - Y
90 - Z
'''

final_data.sort()

total_num = 0

for idx, value in enumerate(final_data) :
    num_sum = 0
    for st in value :
        num_sum += ord(st) - 64
    total_num += (num_sum * (idx+1))
    
        

print(total_num) # 871198282

'''
[The answer]
871198282
'''

