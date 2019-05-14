"""Welcome User"""
i={}
def login():
    global i
    a=input("Enter your user id: ")
    if a in i:
        b=input("Enter password: ")
        if i[a]==b:
            print("Welcome ....")  #change to menu()
        else:
            print("Try again")
    else:
        print("Wrong id, Try again")
def account():
    global i
    a=input("Enter Your name: ")
    b=input("Enter your number: ")
    while True:
        c=input("Enter userid :")
        if c in i:
            print("User id exs: ")
        else:
            d=input("Enter your password: ")
            break
    i[c]=d
print("Welcome to xyz")
while True :
    q=input("Do you have account? ")
    q.upper()
    if q=="Y" or q=="YES":
        login()
    elif q=="N" or q=="NO":
        account()
        
