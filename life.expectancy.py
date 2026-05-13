#APP FOR LIFE EXPECTANCY
#using the simple if statement
#using the while loop to keep asking the user for input till they exit the app

while True:
   age = int(input("Please Enter your age (or -1 to exit):"))

   if age == -1:
        print("See you another time :) ")
        break

   if age == 0:
      print("You have a life expectancy of 63.28 years more")

   elif age >= 1 and age <= 4:
        print("You have a life expectancy of 65.26 years more")

   elif age >= 5 and age <= 9:
       print("You have a life expectancy of 62.14 years more")

   elif age >= 10 and age <= 14:
        print("You have a life expectancy of 57.61 years more")

   elif age >= 15 and age <= 19:
        print("You have a life expectancy of 52.92 years more")

   elif age >= 20 and age <= 24:
        print("You have a life expectancy of 48.50 years more")

   elif age >= 25 and age <= 29:
        print("You have a life expectancy of 44.29 years more")

   elif age >= 30 and age <= 34:
        print("You have a life expectancy of 40.02 years more")

   elif age >= 35 and age <= 39:
        print("You have a life expectancy of 35.72 years more")

   elif age >= 40 and age <= 44:
        print("You have a life expectancy of 31.32 years more")

   elif age >= 45 and age <= 49:
        print("You have a life expectancy of 27.13 years more")

   elif age >= 50 and age <= 54:
        print("You have a life expectancy of 23.07 years more")

   elif age >= 55 and age <= 59:
        print("You have a life expectancy of 19.31 years more")

   elif age >= 60 and age <= 64:
        print("You have a life expectancy of 15.71 years more")

   elif age >= 65 and age <= 69:
        print("You have a life expectancy of 12.54 years more")

   elif age >= 70 and age <= 74:
        print("You have a life expectancy of 9.88 years more")

   elif age >= 75 and age <= 79:
        print("You have a life expectancy of 7.92 years more")

   elif age >= 80:
        print("You have a life expectancy of 7.40 years more")

   else:
        print("Age is out of supported range")
