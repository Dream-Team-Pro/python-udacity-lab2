# Task 1:
# You are required to complete the function reverse(x). given a string "x" as an input it is expected to return that same string but reversed.
# Example:
# input : "again"
# output: "niaga"
# you can change the string value in the variable text but you are not allowed to change the variable names or edit any other code, please only complete the function's definition.
# ______________________________________________________________________________________________
text = "test to reverse string"
def reverse(x):
    #complete this function so that it takes string x as an input 
    #and returns its reverse
    new_str = "" 
    for a in x:
        new_str = a + new_str
    return new_str  

print("reversed string is: "+reverse(text))
