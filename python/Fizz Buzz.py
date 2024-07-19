value = int(input("Enter a number here: "))

if(value%3==0 and value%5!=0):
    print("Fizz")

elif(value%5==0 and value%3!=0):
    print("Buzz")

elif(value%3==0 and value%5==0):
    print("Fizz-Buzz")

else:
     print(value) 