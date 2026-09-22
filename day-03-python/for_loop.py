#1.for loop
for a in range(501):
    print(a)
print("-------------------------")

#2.for loop
name = input("Enter your name: ")
for b in name:
    print(b)
print("-------------------------")

#3.for loop
name = input("Enter your name: ")
for c in name:
    print(c , end= ",")
print("")
print("-------------------------")

#4.for loop
List = ["kiya","op","alex","stive"]
for d in List:
    print(d)
    for e in d:
        print(e,end=",")
print("")
print("-------------------------")

#5.for loop
dictionary = {"supra": "15m",
              "Bugati": "20m",
              "lambo": "9m"}
for f in dictionary:
    print(f)