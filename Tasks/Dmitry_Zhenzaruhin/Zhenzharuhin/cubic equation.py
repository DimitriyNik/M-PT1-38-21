

a=float(input('Введите значение А:'))
b=float(input('Введите значение B:'))
c=float(input('Введите значение C:'))
d=float(input('Введите значение D:'))
disc=-4*b**3*d-4*a*c**3+18*a*b*c*d-27*a**2*d**2
if a==0 and b==0 and c==0 and d==0:
    print("неправильный ввод")
elif disc>0:
    print('уравнение имеет 3 корня')
elif disc<0:
    print('уравнение имеет 1 вещественный корень')
elif disc==0:
    print('в уравнении два корня совпадают')

p=-b**2/(3*a**2)+c/a
q=(2*b**3)/(27*a**3)-(b*c)/(3*a**2)+d/a      
Q=(p/3)**3+(q/2)**2
alfa=(-q/2+Q**(1/2))**(1/3)  #не разобрался как извлекать корень из отрицитального числа
beta=(-q/2-Q**(1/2))**(1/3)

y1=alfa+beta
y2=-(alfa+beta)/2+(3**(1/2)*(alfa-beta)/2)
y3=-(alfa+beta)/2-(3**(1/2)*(alfa-beta)/2)

#print("x1= " +y1-b/(3*a))
#print("x2= " +y2-b/(3*a))
#print("x2= " +y2-b/(3*a))

if Q>0:
    print("x= " +y1-b/(3*a))
    print("x= " +y2-b/(3*a))
    print("x= " +y2-b/(3*a))
elif Q<0:
    print("x1= " +y1-b/(3*a))
    print("x2= " +y2-b/(3*a))
    print("x3= " +y2-b/(3*a))
elif Q==0 and alfa==beta:
    float(y1=2*alfa)
    float(y2=-alfa)
    print("x1= " +y1-b/(3*a))
    print("x2= " +y2-b/(3*a))












