def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)


# note that declaration order is not important as long as call order is respected

def division_by(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('Error:invalid arg, you can\'t divide by 0')
    except:
        print('Error')
    else:
        print("No error occurred")
    finally:
        print("You called the division function.")