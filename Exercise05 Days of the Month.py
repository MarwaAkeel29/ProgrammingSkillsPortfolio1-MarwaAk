#Exercise 5: Days of the Month

#Creaing a dictionary where the keys are month numbers and the values are the number of days in those months.
days_of_the_months = {
    1:31, #Jan
    2:29, #Feb
    3:31, #Mar
    4:30, #Apr
    5:31, #May
    6:30, #June
    7:31, #July
    8:31, #Aug
    9:30, #Sep
    10:31,#Oct
    11:30,#Nov
    12:31 #Dec
}

#Asking the user to input the month number
month = int(input("Enter a month number: ")) #asking user to input a month number.
if month in days_of_the_months:   #using if-else statement as there is more than one condition.
    print("There are", days_of_the_months[month], "Days in month",month)
else:    
    print("Please enter valid month number!")


#Advanced Requirement:

leap_year = input("Is it a leap year? ")  #Asking user if the year is a leap year.
if leap_year.lower() == "yes".lower():   #adding .lower() so all upper cases will convert to lower cases
    print("There are 29 days in february (leap-year)")
else:
    print("There are 28 days in february")

    
