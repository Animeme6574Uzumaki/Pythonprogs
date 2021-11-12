"""
i=6
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    if(i==44):
        i=i+1
        break
    i=i+1
"""

while(True):
    n1 = int(input("Plz enter a number"))
    if n1>100:
        print("CONGRATULATIONS!")
        break
    else:
        print("TRY AGAIN!")
        continue
