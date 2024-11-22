#Exercise 4: Primitive Quiz

Question = input("What is the capital of France? ") #asking user to input the capital of France
if Question.lower()== "Paris".lower(): #using if-else statement as there is more than one condition 
    print("Your answer is CORRECT","Well done!")
else:
    print("Your answer is WRONG!")    


#Advanced Requirements:
name = (input("Enter your name here! ")) #asking user to input their name.
print("Hello!",name, " Welcome to a small quizz,","let's Answer the Capitals of 10 Europian Countries") 
points = 0 #This is the initial points

print("Question 1") 

Question1 = input("What is the capital of United Kingdom? ")
if Question1.lower()== "london".lower(): #using .lower() so that all upper case will be converted to lower case
    print("Your answer is CORRECT","Impressive")
    points += 1 #if the answer is correct it will add 1 point to the initial points.
else:
    print("Your answer is WRONG!") 

print("Question 2")

Question2 = input("What is the capital of Italy? ")
if Question2.lower()== "Rome".lower():
    print("Your answer is CORRECT","Amazing")
    points += 1
else:
    print("Your answer is WRONG!", "keep going!")

print("Question 3") 

Question3 = input("What is the capital of Spain? ")
if Question3.lower()== "Madrid".lower():
    print("Your answer is CORRECT","fantastic")
    points += 1
else:
    print("Your answer is WRONG!", "You can still do better")

print("Question 4")    

Question4 = input("What is the capital of Germany? ")
if Question4.lower()== "Berlin".lower():
    print("Your answer is CORRECT","Well done")
    points += 1
else:
    print("Your answer is WRONG!", "Its never too late")

print("Question 5")   

Question5 = input("What is the capital of Russia? ")
if Question5.lower()== "Moscow".lower():
    print("Your answer is CORRECT","superb")
    points += 1
else:
    print("Your answer is WRONG!","Better luck next time!")

print("Question 6")  

Question6 = input("What is the capital of Switzerland? ")
if Question6.lower()== "Bern".lower():
    print("Your answer is CORRECT","Hats off")
    points += 1
else:
    print("Your answer is WRONG!","keep going!")

print("Question 7")   

Question7 = input("What is the capital of Bulgaria? ")
if Question7.lower()== "Sofia".lower():
    print("Your answer is CORRECT","hurray!")
    points += 1
else:
    print("Your answer is WRONG!","you can do it commom!")

print("Question 8")  

Question8 = input("What is the capital of Norway? ")
if Question8.lower()== "Oslo".lower():
    print("Your answer is CORRECT","2 more to go!")
    points += 1
else:
    print("Your answer is WRONG!","keep going")

print("Question 9")  

Question9 = input("What is the capital of Ireland? ")
if Question9.lower()== "Dublin".lower():
    print("Your answer is CORRECT","awesome!")
    points += 1
else:
    print("Your answer is WRONG!", "Almost there!")

print("Question 10")   

Question10 = input("What is the capital of Finland? ")
if Question10.lower()== "Helsinki".lower():
    print("Your answer is CORRECT","fabulous!")
    points += 1
else:
    print("Your answer is WRONG!","try again!")

print("well done!!! quiz completed!!!")
print(f"Your total points are {points}/10") #this will display the final points.

