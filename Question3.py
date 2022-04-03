#using Python for lab question 2B and 2C

#use dictionary

Modules = {
    "CSC1010":"COMPUTER NETWORKS",
    "CSC1009":"OBJECT-ORIENTED PROGRAMMING",
    "CSC1008":"DATA STRUCTURES AND ALGORITHM",
    "CSC1007":"OPERATING SYSTEMS",
    "CSC1006":"MATHEMATICS 2"
}

def Mod(Modcode):
    if Modules.get(Modcode) is None:
        return "Error: no such module"

    return Modules[Modcode]

print("Question 2B: Enter the module code. Eg. CSC1005: ")
Modcode = input()
print(Mod(Modcode))

#Question 2C, print odd num only
print("Question 2C: ")
for x in range(102,66,-1):
    if x % 2 !=0:
        print("Value of x is: ", x)