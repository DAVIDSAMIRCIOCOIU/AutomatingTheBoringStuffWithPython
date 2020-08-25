def collatz(number):
    try:
        number = int(number)
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        else:
            print(3*number+1)
            return  3*number+1
    except:
        print('You must enter a number.')

myVal = 0
while myVal != 1:
    myVal = collatz(input("Please enter an integer: "))
    print(myVal)