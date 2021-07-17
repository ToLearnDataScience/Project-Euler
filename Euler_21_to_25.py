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

