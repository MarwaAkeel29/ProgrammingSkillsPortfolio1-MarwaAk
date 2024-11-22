#Exercise 10: Is it even 

#using def function to identify whether the number is EVEN or ODD.
def Even_Or_Odd(Number):
    if Number == 0:  #using if-else statement as there is more than one condition.
        return f"{Number} is a neutral number but particularly an even number!"
    elif Number % 2 == 0:
        return f"{Number} is an Even number"
    else:
        return f"{Number} is an Odd number"
        
#using main function.    
def main():
    user_input = int(input("Enter a number to verify whether it's an Even or Odd: ")) #asking user to enter a number to check if its even or odd.   
    output = Even_Or_Odd(user_input) 
    print(output)
    
if __name__ == "__main__" : #the main function will be executed.
    main()  
