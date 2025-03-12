#Simple calculater
#1403/5/14


def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def devide(x, y):
    if y!=0:
        return x/y
    else:
        return 'not available.'


print('simple calculater!')
print('what you gonna do?')
print('1. add')
print('2. subtract')
print('3. multiply')
print('4. devide')

while True:

    choice=int(input('please enter one of these numbers for working with calculater 1, 2, 3, 4:'))

    if choice in [1, 2, 3, 4]:
        num1=float(input('please enter the first number:'))
        num2=float(input('please enter the second number:'))

        if choice==1:
            print(add(num1, num2))
        
        elif choice==2:
            print(subtract(num1, num2))

        elif choice==3:
            print(multiply(num1, num2))

        elif choice==4:
            print(devide(num1, num2))

    else:
        print('please choose only these 4 numberssss')


    next_calculation=input('do you still work with me? yes/no')
    if next_calculation.lower()!='yes':
        print('ok, byee')
        break