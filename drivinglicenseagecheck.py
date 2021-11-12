#This programm can be used for checking age before driving licence testing
print("Enter your age")
age=int(input())
if age==18:
    print("We need to check you physically")
elif age<14:
    print("Betaji it is your age to ride a bicycle not to drive a car")
elif age<18:
    print("You are underage")
elif age>100:
    print("PLz stop joking and enter your real age")
elif age>60:
    print("This is not the age to drive uncle/aunty ji")
elif age>18:
    print("You can come and get tested for driving license")