# Task 2:
# You are required to complete the function average(x). where "x" is a list of numbers. the function is expected to return the average from that list.
# Example:
# input : [10,20,30,40]
# output: 25
# you can change the numbers in the list no_list but you are not allowed to change the variable names or edit any other code, please only complete the function's definition.
# ______________________________________________________________________________________
no_list = [22,68,90,78,90,88]

def average(x):
    #complete the function's body to return the average
    x = no_list
    return sum(x) / len(x)

    
print(average(no_list))
