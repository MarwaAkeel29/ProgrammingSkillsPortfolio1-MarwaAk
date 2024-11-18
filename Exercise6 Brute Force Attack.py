#Exercise 6: Brute Force Attack

#Creaing a program that simulates a password entry system
correct_password="12345" #correct password
max_attempts = 5 #Maximum 5 attemps only 
attempts = 0 #current attempts

#using while loop funcion 
while attempts<max_attempts:
    password = input("Enter the password: ") #asking user to input the password here.
    if password == correct_password: #using if-else statement as there is more than one condition.
        print("You are now logged in!")
        break #This will now terminate the execution when the condition is met.
    else:
        attempts += 1
        attempts_left = max_attempts-attempts #this will deduct the no. of attempts made from the maximum given attempts.
        print("Access denied, Try again!","You have",attempts_left,"attemps left") #this statement will specify that the access is denied with the no. of attempts left.
        
        
if attempts == max_attempts: #it means that if the no. of attempts made is equal to maximum attempts.
    print("Maximum login attempts reached.", "The authorities have been alerted") #the user will be notified "it has reached maximum attempts" and authorities have been alerted. 

