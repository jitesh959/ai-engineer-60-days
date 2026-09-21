student = {}
def add_stundent():
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    student[name] = marks
    with open("result.txt","a") as f:
        for key, value in student.items():
            f.write(f"{key} : {value}\n")
def average_marks():
    with open("result.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(": ")
            student[key] = value
    total = 0
    count = 0
    for value in student.values():
        value = int(value)
        total += value
        count += 1
    average = total / count
    print(average)

def highest():
    with open("result.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(": ")
            student[key] = value
    highest_name = max(student, key=student.get)
    print(f'{highest_name} : {student[highest_name]}')

def result():
    with open("result.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(": ")
            student[key] = value
    for name in student:
        value = int(student[name])
        if value >= 35:
            print(f"{name}has passed the exam")
        else:
            print(f"{name}has failed in exam")

def see_all():
    with open("result.txt","r") as j:
        text = j.read()
        print(text)

while True:
    opp = '''\n
    1. add student
    2. average marks
    3. highest marks
    4. result of students
    5. list of students
    '''
    choose = int(input("Enter opption number : "))
    if choose == 1:
        add_stundent()
    elif choose == 2:
        average_marks()
    elif choose == 3:
        highest()
    elif choose == 4:
        result()
    elif choose == 5:
        see_all()
    elif choose == 6:
        break
    else:
        print("please enter valid opption number")