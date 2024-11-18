#Exercise 8: Simple Search
#Creating a list of strings
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

name = "Sam" 
#using if-else statement as there is more than one condition.
if name in Names: #Looking for a name in the list
    print("Yes the name is in the list")
else:
    print("Sorry! this name is not in ths list")   

#Optional Requirements:
search = input("Enter a name you would like to search: ").lower()  #asking user to input a name in order to search in the given list and adding .lower() to convert uppercase to lower case.
if search.lower() in (name.lower() for name in Names): #adding .lower() so that all upper case will be converted to lower case.
   print("Yes the name is in the list")
else:
    print("Sorry! this name is not in ths list")
