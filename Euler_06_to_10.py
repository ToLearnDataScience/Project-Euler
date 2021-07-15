# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:47:27 2021

@author: 82108
"""

"""
No.6 [Sum square difference]

The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def Sum_Square_dif(number) :
    
    sum_square = 0
    sum_num = 0
    
    for i in range(1, number + 1) :
        square = i ** 2
        sum_square += square
    
    for j in range(1, number + 1) :
        sum_num += j
    
    return (sum_num**2) - sum_square

a = Sum_Square_dif(100)
print(a) # 25164150










"""
No.7 [10001st prime]

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def find_nth_prime(nth) :
    if nth == 1 :
        result = 2
    else :
        cnt = 2
        result = 3
        num = 4
        
        while cnt < nth :
            for i in range(2, num) :
                if num % i == 0 :
                    num += 1
                    break
                if i == (num -1) :
                    result = num
                    num += 1
                    cnt += 1 
                    
    return result


a = find_nth_prime(10001)
print(a) # 104743










"""
No.8 []

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

num_group = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""


str_list = []

for s in num_group :
    str_list.append(s)
        
s_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

final_list = []

for s in str_list :
    if s in s_list :
        final_list.append(s)

len(final_list) # 1000
print(final_list)

cnt = 0
answer_list = []
while cnt < 987 :
    mul = 1
    for i in range(cnt, cnt + 13) :
        num = int(final_list[i])
        mul *= num
    cnt += 1
    answer_list.append(mul)


        
print(answer_list)

max(answer_list)
# 23514624000











"""
No.9 [Special Pythagorean triplet]

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Conditions
1) a^2 + b^2 = c^2
2) a < b < c 
3) a + b + c = 1000
"""

import math


def Find_Pyth(number) :
    
    a = 1
    b = 2
    result = 0
    for i in range(a, number + 1) :
        for j in range(b, number + 1) :
            if i > j :
                pass
            else :
                square_sum = i**2 + j**2
                root_sum = math.sqrt(square_sum)
                if math.trunc(root_sum) == math.sqrt(square_sum) :
                    c = root_sum
                    
                    if i + j + c == 1000 :
                        a = i
                        b = j
                        result = a*b*c
                        break
        
        if result != 0 :
            break
    
    return a, b, c, result

answer = Find_Pyth(1000)

print(answer) # (200, 375, 425.0, 31875000.0)










"""
No.10 [Summation of primes]

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

"""
Using the "Sieve of Eratosthenes"
"""

import math

def Eratosthenes_sum(number) :
    
    answer = 0
    
    result = [True] * number
    root_num = int(math.sqrt(number))
    
    for i in range(2, root_num + 1) :
        for j in range(i+i, number, i) : # j = multiples of i
            result[j] = False
    
    prime_list = [k for k in range(2, number) if result[k] == True]
    
    for l in prime_list :
        answer += l
    
    return answer
    
            
a = Eratosthenes_sum(2000000)
print(a) # 142913828922
























    




