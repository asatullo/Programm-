number = int( input('Plese enter the Total Number of list Elements:'))
a = []
for i in range (number):
    i += 1
    numbers = int( input('Plese enter the Value of {0} Elements:' .format(i)))
    if (numbers % 2 != 0):
        a.append(numbers)
print (a)
