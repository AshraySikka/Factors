x=int(input("Enter a number to find all the factors: "))
for i in range(1,x+1):
    if x%i==0:
        print(i)

