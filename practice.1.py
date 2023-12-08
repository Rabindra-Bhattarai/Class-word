#1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a=5
b=3
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")


#2.  Print "Hello" if a is equal to b, or if c is equal to d.


a=1
b=1
c=2
d=2
if a==b or d==c:
    print("Hello")
   

#3. Print "Hello" if a is equal to b, and c is equal to d.

a=1
b=1
c=2
d=2
if a==b and d==c:
    print("Hello")


#4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.

a=int(input("Enter any number: "))
if a>=0:
    print("Positive")
else:
    print("Negative")


#5. Check whether the user input number is even or odd and display it to user.

a=int(input("Enter any number: "))

if (a % 2)==0:
    print("Even")
else:
    print("Odd")

#6. WAP(write a program) which accepts marks of four subjects and display total marks, percentage and grade.
 
marks=[50,60,70,80]
total_marks=sum(marks)
percentage=(total_marks/ (4*100))*100

if percentage >= 90:
  print("A")
elif percentage >= 80:
   print("B")
elif percentage >= 70:
   print("c")
elif percentage >= 60:
   print("D")
else:
   print("E")

#7. What is the output of ‘APPLE’ > ‘apple’?

print('APPLE' > 'apple')

