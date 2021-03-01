print("1:length of a string:")
print("2:concatenation of a string:")
print("3:maximum of a string:")
print("4:minimum of a string:")
print("5:to upper of a string:")
print("6:to lower of a string:")
print("7:casefold of a string:")
print("8:capitalize of a string:")
print("9:digit of a string:")
print("10:alpha of a string:")
while True:
    choice=int(input("enter the choice:"))
    if choice==1:
        n1=(input("enter the string:"))
        print(len(n1))
    elif choice==2:
        n1=(input("enter the first string:"))
        n2=(input("enter the second string:"))
        print(n1+n2)
    elif choice==3:
        n1=(input("enter the string:"))
        print(max(n1))
    elif choice==4:
        n1=(input("enter the string:"))
        print(min(n1))
    elif choice==5:
        n1=(input("enter the string:"))
        print(n1.upper())
    elif choice==6:
        n1=(input("enter the string:"))
        print(n1.lower())
    elif choice==7:
        n1=(input("enter the string:"))
        print(n1.casefold())
    elif choice==8:
        n1=(input("enter the string:"))
        print(n1.capitalize())
    elif choice==9:
        n1=(input("enter the string:"))
        print(n1.isdigit())
    elif choice==10:
        n1=(input("enter the string:"))
        print(n1.isalpha())
        break
    else:
        print("invalid choice!!!")