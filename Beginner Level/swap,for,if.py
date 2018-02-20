#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     20/02/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
    #swap program
x = 12
y = 18
x = y
y = x
print(x,y)
     #for loop ex1
x = 1
y = "2"
z = 3
sum = 0
for i in (x,y,z):
    if isinstance(i, int):
        sum += i
print sum
    #for loop ex2
x=0
for i in range(2, 10, 2):
    x = x + i
    print(x)

    #if else
colors = ['Red', 'Black', 'White', 'Green']
if "green" in colors:
   print("Green Color")
else:
   print("No Green Color")
    #ex
x = 1
print(++++x)

