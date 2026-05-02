num = int(input("Enter number to check :"))

if num > 50 :
    print("Your number is greater than 50")
    if num%2==0 :
        print("And it's even too")
    else:
       print("And it's odd too") 
else:
    print("Your number is smaller than 50")