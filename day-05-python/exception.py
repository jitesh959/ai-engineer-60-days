def table():
    try:
        n = int(input("Enter a number: "))
        for i in range(1,11):
            print(f"{n} X {i} = {n*i}")
    except:
        print("somthing went wrong")
        table()
    finally:
        print("thank you")
table()

try:
    num = int(input("Enter a number: "))
    print(num)
except NameError:
    print()
except IndexError:
    print()
except IndentationError:
    print()
except Exception as e:
    print(e)
finally:
    print("this will always execute")