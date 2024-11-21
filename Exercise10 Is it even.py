#Exercise 10: Is it even?
def Even_Or_Odd(Number):
    if Number == 0:
        return f"{Number} is a neutral number but particularly an even number!"
    elif Number % 2 == 0:
        return f"{Number} is an Even number"
    else:
        return f"{Number} is an Odd number"
    
def main():
    user_input = int(input("Enter a number to verify whether it's an Even or Odd: "))    
    output = Even_Or_Odd(user_input)
    print(output)\
    
if __name__ == "__main__" :
    main()  