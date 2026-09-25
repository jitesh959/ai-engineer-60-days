opp = '''1. Add expens
2. viwe expens
3. Exit
'''
def app():
    try :
        print(opp)
        choose = int(input("Enter choose: "))
        if choose == 1:
            item = input("Enter Expens name: ")
            cost = int(input("Enter amount: "))
            with open ("Expens.txt","a") as a:
                a.write(f"{item}: {cost}\n") 
                app()   
        elif choose == 2:
            with open("Expens.txt","r") as b:
                c = b.read()
                print(c)
                app()
        elif choose == 3:
            print("Thank you")
    except:
        print("somthing went worng")
        print("try again\n")
        app()
app()