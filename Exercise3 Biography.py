#Exercise3 Biography.py

#creating a dictionary with my details
informaion = {
    "Name": "Marwa Akeel",
    "Hometown": "Sharjah",
    "Age": "18"
}

for key, value in informaion.items(): #Using for function and key-value pairs.
    print(f"{key}: {value}")  #This will print the information in seperate lines.


#Advanced Requirements:
name = input("Enter your Name: ") #asking user to input their name.
hometown = input("Enter your Hometown: ") #asking user to input their hometown.
age = input("Enter your Age: ") #asking user to input their age (incase if the user enters string value for age, it is acceptable.)

#creating a dictionary for user's personal_info
personal_info = {
    "Name" : name,
    "Hometown" : hometown,
    "Age" : age
}

for key, value in personal_info.items(): #using for funcion and key-value pairs.
    print(f"{key}: {value}") #This will print the personal_info in seperate lines.