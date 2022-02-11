# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from StackArray import Stack

def is_valid(expr):
    st = Stack()
       
    for ch in expr:
        if ch in '({[':
            st.push(ch)
        if ch in ')}]':
            if st.is_empty():
                print("Right parentheses are more than left parentheses")
                return False
            else:
                char = st.pop()
                if not match_parentheses(char,ch):
                    print("Mismatched parentheses are ", char , " and " , ch)
                    return False
                
    if st.is_empty():
        print("Balanced Parentheses")
        return True
    else:
        print("Left parentheses are more than right parentheses")
        return False 
	  	    
def match_parentheses(left_par, right_par):
    if  left_par == '[' and right_par == ']':
        return True 
    if  left_par == '{' and right_par == '}':
        return True 
    if  left_par == '(' and right_par == ')':
        return True 
    return False 


#############################################################################

while True:
    print("Enter an expression with parentheses (q to quit) : ", end = ' ')
    expression = input()

    if expression == "q":
        break

    if is_valid(expression):
        print("Valid expression")
    else:
        print("Invalid expression")





