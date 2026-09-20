s_name = input("Enter student name: ")
s_marks = int(input("enter student marks: "))

if s_marks >= 90:
    print(s_name, "has opptaned Excellent marks",s_marks)
elif s_marks >= 75:
    print(s_name, "has opptaned very good marks",s_marks)
elif s_marks >= 60:
    print(s_name, "has opptaned good marks",s_marks)
elif s_marks >= 45:
    print(s_name, "has opptaned passing marks",s_marks)
elif s_marks >= 35:
    print(s_name, "has opptaned vjust passing marks",s_marks)
else:
    print(s_name ,"has failed in exam",s_marks)
