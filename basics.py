college={
     "aml":{
        "name":"artificial intelligence and machine learning",
        "code":1310
             },

    "ads":{
        "name":"artificial intelligence and data science",
        "code":1320
    },
    "cse":{
        "name":"computer science and engineering",
        "code":1330
    },
    "it":{
        "name":"Information Technology",
        "code":1340
    },
}
print(college["aml"]["name"])



# Taking input marks for subjects
OS = int(input("Enter the OS mark: "))
DBDS = int(input("Enter the DBDS mark: "))
DAA = int(input("Enter the DAA mark: "))
DTT = int(input("Enter the DTT mark: "))

# Calculating the average of the marks
average cls= (OS + DBDS + DAA + DTT) / 4

    #Calculator
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
operations=input("Enter operation(Addition,Subtraction,Multiplication,Division):")
if(operations=="Addition"):
    print("Addition",a+b)
elif(operations=="Subtraction"):
    print("Subtraction",a-b)
elif(operations=="Multiplication"):
    print("Multiplication",a*b)
elif(operations=="Division"):
    if(b!=0):
        print("Dvision",a/b)
    else:
        print("Division by zero is invalid")
else:
    print("Invalid operation")