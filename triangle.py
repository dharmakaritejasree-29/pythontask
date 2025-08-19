def triangle():
    a=int(input('enter a value '))
    b=int(input('enter b value '))
    c=int(input('enter c value '))
    if a<b+c and b < c+a and c < a+b:
        print('triangle')
        if a==b==c:
            print('equilateral triangle')
        elif a==b!=c or b==c!=a or a==c!=b:
            print('isosceles triangle')
        elif a**2==b**2 + c**2 or b**2==a**2 + c**2 or c**2 == a**2 + b**2:
            print('right angled triangle')
        else:
            print('scalene triangle')
    else:
        print('do not form a triangle')
        
triangle()