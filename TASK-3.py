# Task 3:
# You are required to complete the function maximum(x). where "x" is a list of numbers. the function is expected to return the highest number in that list.
# Example:
# input : [5,20,12,6]
# output: 20
# you can change the numbers in the list no_list but you are not allowed to change the variable names or edit any other code, please only complete the function's definition.
# _______________________________________________________________________________
no_list = [1,2,3,4]

def maximum(no_list):
    #complete the function to return the highest number in the list
    max = 0
    for i in no_list:
        if i > max:
            max = i
    return max


print(maximum(no_list))
