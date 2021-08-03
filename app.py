##############################################################
# this application tells you the grade from your percentage..#
##############################################################

percentage = input("enter your percentage: ")  # to get input from user

percentage = int(percentage)  # to transfer string value into integer value

if percentage >= 90:
    print("Your grade is: Excellent")

elif 85 <= percentage < 90:
    print("Your grade is: Very Good")

elif 75 <= percentage < 85:
    print("Your grade is: Good")

elif 50 <= percentage < 75:
    print("Your grade is: passed")

elif percentage < 50:
    print("Your grade is: Failed")

else:
    print("Sorry Your percentage is not correct")
