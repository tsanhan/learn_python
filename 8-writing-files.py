# # we will learn: 
# # reading/writing files
# #  tuples 
# #  recurcive functions

# # ---------- READING & WRITING TEXT ----------

# # The os module provides methods for file processing
# import os
 
# # We are able to store data for later use in files
 
# # You can create or use an already created file with open
 
# # If you use w (write) for mode then the file is
# # overwritten.
# # If you use a (append) you add to the end of the file
 
# # Text is stored using unicode where numbers represent
# # all possible characters
 
# # We start the code with with which guarantees the file
# # will be closed if the program crashes
# with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
 
#     # You can write to the file with write
#     # It doesn't add a newline
#     myFile.write("Some random text\nMore random text\nAnd some more")
 
 
# # Open the file for reading
# # You don't have to provide a mode because it is
# # read by default
# with open("mydata.txt", encoding="utf-8") as myFile:
 
#     # We can read data in a few ways
#     # 1. read() reads everything into 1 string
#     # 2. readline() reads everything including the first newline
#     # 3. readlines() returns a list of every line which includes
#     # each newline
 
#     # Use read() to get everything at once
#     print(myFile.read())
 
# # Find out if the file is closed
# print(myFile.closed)
 
# # Get the file name
# print(myFile.name)
 
# # Get the access mode of the file
# print(myFile.mode)
 
# # Rename our file
# os.rename("mydata.txt", "mydata2.txt")
 
# # Delete a file
# # os.remove("mydata.dat")
 
# # Create a directory
# # os.mkdir("mydir")
 
# # Change directories
# # os.chdir("mydir")
 
# # Display current directory
# print("Current Directory :", os.getcwd())
 
# # Remove a directory, but 1st move back 1 directory
# # os.chdir("..")
# # os.rmdir("mydir")
 
# # ---------- PROBLEM : Fibonacci sequence ----------
# # Previously we generated 1 number in the
# # Fibonacci sequence. This time ask the user to define
# # how many numbers they want and display them
# # The formula for calculating the Fibonacci sequence is
# # Fn = Fn-1 + Fn-2
# # Where F0 = 0 and F1 = 1
 
# # Sample Output
# '''
# How many Fibonacci values should be found : 30
# 1
# 1
# 2
# 3
# 5
# All Done
# '''
 
# def fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         result = fib(num - 1) + fib(num - 2)
#         return result
 
# numFibValues = int(input("How many Fibonacci values should be found : "))
 
# i = 1
 
# # While i is less then the number of values requested
# # continue to find more
# while i < numFibValues:
 
#     # Call the fib()
#     fibValue = fib(i)
 
#     print(fibValue)
 
#     i += 1
 
# print("All Done")
 
 
# # ---------- READ ONE LINE AT A TIME ----------
# # You can read 1 line at a time with readline()
 
# # Open the file
# with open("mydata2.txt", encoding="utf-8") as myFile:
 
#     lineNum = 1
 
#     # We'll use a while loop that loops until the data
#     # read is empty
#     while True:
#         line = myFile.readline()
 
#         # line is empty so exit
#         if not line:
#             break
 
#         print("Line", lineNum, " :", line, end="")
 
#         lineNum += 1
 
# # ---------- PROBLEM : ANALYZE THE FILE ----------
# # As you cycle through each line output the number of
# # words and average word length
# '''
# Line 1
# Number of Words : 3
# Avg Word Length : 4.7
# Line 2
# Number of Words : 3
# Avg Word Length : 4.7
# '''
 
# with open("mydata2.txt", encoding="utf-8") as myFile:
 
#     lineNum = 1
 
#     while True:
#         line = myFile.readline()
 
#         # line is empty so exit
#         if not line:
#             break
 
#         print("Line", lineNum)
 
#         # Put the words in a list using the space as
#         # the boundary between words
#         wordList = line.split()
 
#         # Get the number of words with len()
#         print("Number of Words :", len(wordList))
 
#         # Incremented for each character
#         charCount = 0
 
#         for word in wordList:
#             for char in word:
#                 charCount += 1
 
#         # Divide to find the answer
#         avgNumChars = charCount/len(wordList)
 
#         # Use format to limit to 2 decimals
#         print("Avg Word Length : {:.2}".format(avgNumChars))
 
#         lineNum += 1
 
# ---------- TUPLES ----------
# A Tuple is like a list, but their values can't be changed
# Tuples are surrounded with parentheses instead of
# square brackets
 
myTuple = (1, 2, 3, 5, 8)
 
# Get a value with an index
print("1st Value :", myTuple[0])
 
# Get a slice from the 1st index up to but not including
# the 3rd
print(myTuple[0:3])
 
# Get the number of items in a Tuple
print("Tuple Length :", len(myTuple))
 
# Join or concatenate tuples
moreFibs = myTuple + (13, 21, 34)
 
# Check if a value is in a Tuple
print("34 in Tuple :", 34 in moreFibs)
 
# Iterate through a tuple
for i in moreFibs:
    print(i)
 
# Convert a List into a Tuple
aList = [55, 89, 144]
aTuple = tuple(aList)
 
# Convert a Tuple into a List
aList = list(aTuple)
 
# Get max and minimum value
print("Min :", min(aTuple))
print("Max :", max(aTuple))

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#A tuple can also be created without using parentheses. This is known as tuple packing.
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

# Creating a tuple with one element is a bit tricky.
# add comma to indicate that it is, in fact, a tuple.

my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>

# ---------- Sets ----------
# https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.hashset-1?view=net-5.0
# https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/set-operations

# Sets are lists with no duplicate entries. 
# Let's say you want to collect a list of words used in a paragraph:


# how to creatre?
# set literal
someSet = {"my", "name", "is", "Eric", "and", "Eric", "is", "my", "name"}
print(someSet)

# from tuple / list
someSet = "my name is Eric and Eric is my name".split()
print(someSet)
someSet = set(("my", "name", "is", "Eric", "and", "Eric", "is", "my", "name"))
print(someSet)
someSet = set(["my", "name", "is", "Eric", "and", "Eric", "is", "my", "name"])
print(someSet)
# This will print out a list containing "my", "name", "is", "Eric", and finally "and".
# Since the rest of the sentence uses words which are already in the set, they are not inserted twice.

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# but not number of mutable elements like lists, sets or dictionaries as its elements.
# my_set = {1.0, "Hello", [3,56]} # error
# my_set = {1.0, "Hello", {3,56}} # error
my_set = {1.0, "Hello", (3,56)} 
print(my_set)

# MODIFING SETS
# Sets are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.

# add a single element
my_set.add(2)
print(my_set)

#add multiple elements
my_set.update([2, 3, 4])
print(my_set)
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Removing elements from a set
# discard() and remove()
# small class exercise: (learn some testing skills) find the difference without searching the internet!

# SOLUTION: on not present value remove() will raise an error.

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

# my_set.remove(2)

# remove some item (can't tell which, the data type is unordered  )
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

# Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between other sets.
# For example, say you have a list of participants in events A and B:

# Python Set Operations
# two a group of two sets
'''
        *********  A
        *       *
    *********   *
    *   *   *   *
 B  *   *********
    *       *
    *********
'''

#------ Set Union ----- 
# Union of A and B is a set of all elements from both sets.
'''
        *********  A
        *********
    *************
    *************
B   *************
    *********
    *********
'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B) 
# OR
print(A.union(B))
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# ------ Set Intersection ------
# Intersection of A and B is a set of elements that are common in both the sets.
'''
        *********  A
        *       *
    *********   *
    *   *****   *
 B  *   *********
    *       *
    *********
'''

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)
print(A.intersection(B))
# {4, 5}

# ------ Set Difference ------
# Difference of the set B from set A(A - B) is a set of elements that are only in A but not in B.
# Similarly, B - A is a set of elements in B but not in A.

'''
        *********  A
        *       *
    *********   *
    *****   *   *
 B  *************
    *********
    *********
'''

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)
A.difference(B)
# Output: {1, 2, 3}


# -------Set Symmetric Difference ---------
# Symmetric Difference of A and B is a set of elements in A and B but not in both (excluding the intersection).
'''
        *********  A
        *********
    *************
    *****   *****
 B  *************
    *********
    *********
'''

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)
A.symmetric_difference(B)
# Output: {1, 2, 3, 6, 7, 8}

my_set = set("apple")
print('a' in my_set)# Output: True
print('p' not in my_set)# Output: False
# Output: True

# HW: Sets deepdive and Frozenset https://realpython.com/python-sets/

# ------ PROBLEM - Letter Combinations of a Phone Number ------
# a real problem that was exsists on phones with numbers as digits:

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons)
# is given below. 
# Note that 1 does not map to any letters.

'''
1(∞)   2(abc) 3(def)
4(ghi) 5(jkl) 4(mno)
7(pqrs)8(tuv) 9(xyz)
       9(‿)
'''

'''
Example 1:
Input: digits = "23"
Output: { "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf" }
                ⋰ d - ad
           a - 3⋯ e - ae
         /      ⋱ f - af
        /       ⋰ d - bd
"23"- 2 -- b - 3⋯ e - be
        \       ⋱ f - bf
         \      ⋰ d - cd
           c - 3⋯ e - ce
                ⋱ f - cf
'''

'''
Example 2:
Input: digits = ""
Output: set()
'''

'''
Example 3:
Input: digits = "2"
Output: { "a", "b", "c" }
'''

'''
Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

# solve recursively AND iteratively