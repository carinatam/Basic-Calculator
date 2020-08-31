def addition_answer(a,b):
    answer=a+b
    return answer #returns answer to addition_answer(x,y)
def subtraction_answer(c,d):
    answer=c-d
    return answer
def multiplication_answer(e,f):
    answer=e*f
    return answer
def division_answer(g,h):
    answer=g/h
    return answer

print("Welcome! This program will calculate addition, subraction, multiplicantion and division of any two numbers")
choice=int(input("Press 1 for addition, 2 for subrtraction, 3 for multiplication, 4 for division, and 5 for exit: "))
while(choice!=5): #as long as they don't exit the program
    if(choice>5 or choice<1): #if user puts something invalid like 6 or -1
        print("This is an invalid command, please try again")
        choice=int(input("Press 1 for addition, 2 for subrtraction, 3 for multiplication, 4 for division, and 5 for exit: ")) #continues program
    x=float(input("Please enter the first number: "))
    y=float(input("Please enter the second number: "))
    if(choice==1): #if it is for addition
        addition=addition_answer(x,y) #refer to def addition_answer
        print("The result of",x,"+",y,"is",addition)
        print()
    elif(choice==2): #if it is for subtraction
        subtraction=subtraction_answer(x,y)#refer to def subtraction_answer
        print("The result of",x,"-",y,"is",subtraction)
        print()
    elif(choice==3): #if it is for multiplication
        multiplication=multiplication_answer(x,y) #refer to def multiplication_answer
        print("The result of",x,"*",y,"is",multiplication)
        print()
        
    elif(choice==4):#if it is for division
        if(y==0): #if denominator is 0 then it is invalid
            print("There is no answer for",x,"/",y,"since the denominator is 0")
            print()
            choice=int(input("Press 1 for addition, 2 for subrtraction, 3 for multiplication, 4 for division, and 5 for exit: ")) #continues program
            x=float(input("Please enter the first number: "))
            y=float(input("Please enter the second number: "))
            if(choice==1):
                addition=addition_answer(x,y)
                print("The result of",x,"+",y,"is",addition)
                print()
            elif(choice==2):
                subtraction=subtraction_answer(x,y)
                print("The result of",x,"-",y,"is",subtraction)
                print()
            elif(choice==3):
                multiplication=multiplication_answer(x,y)
                print("The result of",x,"*",y,"is",multiplication)
                print()
            elif(choice==4):
                division=division_answer(x,y)
                print("The result of",x,"/",y,"is",division)
                print()
        else: #if denominator is not 0
            division=division_answer(x,y) #refer to def division_answer
            print("The result of",x,"/",y,"is",division)
            print()
        
    choice=int(input("Press 1 for addition, 2 for subrtraction, 3 for multiplication, 4 for division, and 5 for exit: ")) #continues program
print("Have a good day!") #if user enters 5
