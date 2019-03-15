## Given an array A[] and a number x, check for pair in A[] with sum as x

# gvarray = [4,3,-7,1,4,8,9]
# sum = 12
#
# sortedarray = gvarray.sort()
#
# for i in gvarray:
#     print(sortedarray[i])
# # initialize two index variables to find the candidate elements
# l = 0
# r = len(gvarray)-1

# while l < r:
#     if gvarray[l] + gvarray[r] == sum:
#         return l
#     elif gvarray[l] + gvarray[r] < sum:
#         l++
#     else:
#         r--

##########*************##################**************#################*********###############

## Find first non-repeating character in a string

# char_map = {}
# non_repeating_chars = []
#
# def firstNonRepeating(str):
#     for c in str:
#         if c in char_map:
#             char_map[c] = True
#             non_repeating_chars.append(c)
#         else:
#             char_map[c] = True
#
# if __name__ == "__main__":
#     str = "GeeksForGeeks"

##########*************##################**************#################*********###############
## Find largest number in a list
# def createList(num_of_elements):
#     for i in range(1, num_of_elements + 1):
#         element = int(input("Element to add: "))
#         num_list.append(element)
#     return num_list
#
#
# def findMax(num_list):
#     max = num_list[0]
#     for x in num_list:
#         if x > max:
#             max = x
#     return max
#
#
# if __name__ == "__main__":
#     num_list = []
#     num_of_elements = int(input("Elements in list: "))
#     createList(num_of_elements)
#     print("Largest element in your list of numbers is: ", findMax(num_list))

##########*************##################**************#################*********###############

## Print digits of a number in a pattern

# def printPattern(numArray):
#     n = len(numArray)
#     if n%2 == 0:
#         for i in range(int(n/2)):
#             print('{}{}'.format(numArray[i], numArray[n-1-i]),end='')
#     elif n%2 != 0:
#         for i in range(int(n/2)):
#             print('{}{}'.format(numArray[i], numArray[n-1-i]),end='')
#         print('{}'.format(numArray[int(n/2)]))
#
# if __name__ == "__main__":
#     number = input("Enter Number: ")
#     digits = [int(x) for x in str(number)]
#     printPattern(digits)

##########*************##################**************#################*********###############











