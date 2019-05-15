"""Welcome User"""
i={}
l=[]
def login():        #func login
    global i
    global ch
    global us
    a=input("Enter your user id: ")
    if a in i:
        b=input("Enter password: ")
        if i[a]==b:
            ch,us=menu(a)  #menu()
        else:
            print("Try again")
    else:
        print("Wrong id, Try again")            #func login end
def account():              #func account
    global i
    global l
    global ch
    global us
    e={}
    a=input("Enter Your name: ")
    b=int(input("Enter your number: "))
    f=input("Enter your mail id-> ")
    while True:
        c=input("Enter userid :")
        if c in i:
            print("User id exs: ")
        else:
            d=input("Enter your password: ")
            i[c]=d
            e["Name"]=a
            e["Number"]=b
            e["mail"]=f
            e["User_id"]=c
            e["Passw"]=d
            l.append(e)
            print("Welldone, Your account has been created")
            ch,us=menu(c)
            break                           #func account end
def menu(x):                    #func menu 
    print("*"*50)
    for i in l:
        if i["User_id"]==x:
            break
    n=i["Name"]
    no=i["Number"]
    print("Welcome %s your phone number is- %d"%(n,no))
    print()
    print("1. Edit your information \n2.Add biodata \n3.Change Password \n4. Exit")
    a=int(input("Pleace select your choice -> "))               #func menu end
    return a,x
def edit(y):                    #func edit
    global l
    d=0
    for i in l:
        if i["User_id"]==y:
            break
        d+=1
    print("Name- ",i["Name"])
    print("Phone number- ",i["Number"])
    print("E-Mail id- ",i["mail"])
    while True:
        b=input("What you want to change? ")
        b=b.upper()
        if b=="NAME":
            c=input("Enter new name- ")
            i["Name"]=c
            l[d]=i
        elif b=="PHONE NUMBER" or b=="NUMBER":
            c=input("Enter new number-> ")
            i["Number"]=c
            l[d]=i
        elif b=="MAIL" or b=="EMAIL":
            c=input("Enter new mail id-> ")
            i["mail"]=c
            l[d]=i
        else:
            print("Select name or number only")
        e=input("Do you want to change any thing else? ")
        e=e.upper()
        if e=="Y" or e=="YES":
            continue
        elif e=="N" or e=="NO":
            break
    print("Your information has beem successfully updated")     #func edit end
def biodata():                  #func biodata
    print(0)
print("Welcome to xyz")
while True :
    print()
    q=input("Do you have an account? ")
    print()
    q=q.upper()
    if q=="Y" or q=="YES":
        login()
        print()
    elif q=="N" or q=="NO":
        print("Lets create your account!!")
        print()
        account()
        print()
    print("Yoiu entered choice number ",ch)
    if ch==1:
        edit(us)
    qq=input("*Do you want to continue?* ")
    qq=qq.upper()
    if qq=="Y" or qq=="YES":
        continue
    elif qq=="N" or qq=="NO":
        break

        
