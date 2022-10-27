y = list()
num = int(input("Enter the range: "))
for x in range(num):
    try:
        y.append(float(input()))
    except ValueError:
        print("You have not entered a number. Please try again by entering a number.")
        break

for x in reversed(y):
    print(x, end=' ')
