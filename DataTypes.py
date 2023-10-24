#two_digit_number = input("Type a two digit number  ")
#first_digit = two_digit_number[0]
#second_digit = two_digit_number[1]
#result= int(first_digit) + int(second_digit)
#print(result)
#height =  input("Enter your height in m ")
#weight = input("Enter your weight in kg ")
#BMI = int(weight)/float(height)**2
#print(BMI)


#age = input(" what is your age ?  ")
#lifetime =90 - int(age)
#days =lifetime * 365
#weeks = lifetime * 52
#months =lifetime * 12
#print("You have " + str(days) + " days, " + str(weeks) + " weeks, "+ str(months) + " months left.")


#TotalBill = input("Type the total bill    ")
#percentage = input("Choose the percentage tip :10, 12, 15,   ")
#people = input("How many people to split the ball?  ")
#percentBill = float(TotalBill)+float(TotalBill)*12
#result =round(percentBill/float(people),2)
#print(result)


#number = int(input("Type your number :  "))
#if (number%2 == 0):
#    print("This number is even")
#else:
#    print("This number is odd ")


#height =  input("Enter your height in m ")
#weight = input("Enter your weight in kg ")
#BMI = int(weight)/float(height)**2
#print(BMI)
#if BMI < 18.5:
#    print("You are underweight")
#elif 18.5<BMI<25:
#    print("You have a normal weight")
#elif 25<BMI<30:
#    print("You are overweight")
#elif 30<BMI<35:
#    print("You are obese")
#else:
#    print("You are clinically obese")

#year = int(input("Which year do you want to check?   "))
#if year%4==0 :
#    if year%100
#    print("this is a leap year")
#else:
#    print("this is not a leap year")


import random

test_seed = int(input("Create a seed number  "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, separated by a comma:   ")
names = namesAsCSV.split(",  ")
x = len(names)
random_index = random.randint(0, (x-1))
print(random_index)
person = names[random_index]

print(person + " is going to pay for this meal ")




