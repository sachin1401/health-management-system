# health management system
# here three paitent you can store data and retrive data

print('Health Management System')
def getdate():
    import datetime
    return datetime.datetime.now()

print('choose client : ')
print('1.Harry 2.Rohan 3.Hammad :')
client=int(input())

if client==1:
    print('You want to 1.lock or 2.reterive:')
    choice=int(input())
    if choice==1:
        print('choose 1.exercise 2.diet :')
        choose=int(input(''))
        if choose==1:
            print(getdate())
            print('What exercise you do enter:')
            f=open('harry.txt','w')
            f.write(input())
            f.close()
        elif choose==2:
            print(getdate())
            print('what did you eat enter:')
            f=open('harrydiet.txt','w')
            f.write(input())
            f.close()
    elif choice==2:
        print('choose 1.exercise 2.diet :')
        choose1=int(input(''))
        if choose1==1:
            print(getdate())
            print('This exercise you do:')
            f=open('harry.txt',"r")
            c=f.read()
            print(c)
            f.close()
        elif choose1==2:
            print(getdate())
            print('This is your diet:')
            f=open('harrydiet.txt',"r")
            c=f.read()
            print(c)
            f.close()  

#client-2
elif client==2:
    print('You want to 1.lock or 2.reterive:')
    choice=int(input())
    if choice==1:
        print('choose 1.exercise 2.diet :')
        choose=int(input(''))
        if choose==1:
            print(getdate())
            print('What exercise you do enter:')
            f=open('rohane.txt','w')
            f.write(input())
            f.close()
        elif choose==2:
            print(getdate())
            print('what did you eat enter:')
            f=open('rohand.txt','w')
            f.write(input())
            f.close()
    elif choice==2:
        print('choose 1.exercise 2.diet :')
        choose1=int(input(''))
        if choose1==1:
            print(getdate())
            print('This exercise you do:')
            f=open('rohane.txt',"r")
            c=f.read()
            print(c)
            f.close()
        elif choose1==2:
            print(getdate())
            print('This is your diet:')
            f=open('rohand.txt',"r")
            c=f.read()
            print(c)
            f.close()   


#client-3
elif client==3:
    print('You want to 1.lock or 2.reterive:')
    choice=int(input())
    if choice==1:
        print('choose 1.exercise 2.diet :')
        choose=int(input(''))
        if choose==1:
            print(getdate())
            print('What exercise you do enter:')
            f=open('hammade.txt','w')
            f.write(input())
            f.close()
        elif choose==2:
            print(getdate())
            print('what did you eat enter:')
            f=open('hammadd.txt','w')
            f.write(input())
            f.close()
    elif choice==2:
        print('choose 1.exercise 2.diet :')
        choose1=int(input(''))
        if choose1==1:
            print(getdate())
            print('This exercise you do:')
            f=open('hammade.txt',"r")
            c=f.read()
            print(c)
            f.close()
        elif choose1==2:
            print(getdate())
            print('This is your diet:')
            f=open('hammadd.txt',"r")
            c=f.read()
            print(c)
            f.close()   


