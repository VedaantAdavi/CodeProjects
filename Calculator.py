#Importing math library
import math

#Create a class for Basic arithmetic operations
class operations:
    def add(x):
        x=int(input("\nType in a number"))
        x2=int(input("Type in another number"))
        result=print(x+x2,"\n")
        return result
    def subtract(x):
        x=int(input("\nType in a number"))
        x2=int(input("Type in another number"))
        result=print(x-x2,"\n")
        return result
    def multiply(x):
        x=int(input("\nType in a number"))
        x2=int(input("Type in another number"))
        result=print(x*x2,"\n")
        return result
    def divide(x):
        x=int(input("\nType in a number"))
        x2=int(input("Type in another number"))
        result=print(x/x2,"\n")
        return result

#Create a class for squaring functions
class squares:
    def square(x):
        x=int(input("\nType in a number"))
        result=print(x*x,"\n")
        return result
    def sqrt(x):
        x=int(input("\nType in a number"))
        result = print(math.sqrt(x),"\n")
        return result
        
#Create a class for trigometric functions
class trig:
    def Sin_Cos_Tan(x):
        userinput2=int(input("1.Sin\n2.Cos\n3.Tan"))
        if userinput2==1:
            x=int(input("\nType in a number"))
            result=print(math.sin(x),"\n")
            return result
        if userinput2==2:
            x=int(input("\nType in a number"))
            result=print(math.cos(x),"\n")
            return result
        if userinput2==3:
            x=int(input("\nType in a number"))
            result=print(math.tan(x),"\n")
            return result
	
        

#Initialize the classes
operations=operations()
squares=squares() 
trig=trig()
    

#Ask the user what they want to do
userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))

#While the user does not type in 8, run the code
while userinput != 9:
    
    #If the user chooses 1, call the add function from the operations class
    if userinput==1:
        operations.add()
        userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
    
    #If the user chooses 2, call the subtract function from the operations class
    if userinput==2:
        operations.subtract()  
        userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
   
    #If the user chooses 3, call the multiply function from the operations class
    if userinput==3:
        operations.multiply() 
        userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
    
    #If the user chooses 4, call the divide function from the operations class
    if userinput==4:
        operations.divide()
        userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
   
    #If the user chooses 5, call the square function from the squares class
    if userinput==5:
        squares.square()
        userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
   
   #If the user chooses 6, call the sqrt function from the squares class
    if userinput==6:
        squares.sqrt()
        userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
        
    #If the user chooses 7, call the Sin_Cos_Tan function from the trig class
    if userinput==7:
        trig.Sin_Cos_Tan()
        userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
    #If the user chooses 8, ask them to type in a full expression, then calculate and print the solution
    if userinput==8:
        x=input("Type in an expression, type in done to exit this option")
        if x=="done":
            userinput=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Square Root\n7.Sin/Cos/Tan\n8.Expression Calculator\n9.Done"))
        else:
            r=eval(x)
            print(r)
    #If the user types in 8, print Thank you for using this software
    if userinput==9:
        break



