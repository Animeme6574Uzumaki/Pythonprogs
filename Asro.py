print("Astrologer's star")
nrow = int(input("How many rows do you want to print?:\n"))
pattern = "*"
bool9 = bool(int(input("Enter 1 for increasing triangle pattern and 0 for decreasing triangle pattern")))
if bool9:
    for i in range(nrow):
        for j in range(i + 1):
            print("*", end=" ")
        print()
if not bool9:
    for i in range(nrow):
        for j in range(i, nrow):
            print("*", end=" ")
        print()
