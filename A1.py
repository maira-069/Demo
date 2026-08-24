print(   "-----STUDENT RESULT-----"   )
a=str(input("Name:"))
b=float(input("English:"))
c=float(input("Mathematics:"))
d=float(input("Computer Science:"))
e=float(input("Pyscis:"))
f=float(input("Chemistry:"))
total_marks=b+c+d+e+f 
percentage=(b+c+d+e+f)*100/500.0

print ("Total Marks are:",total_marks)
print("Percentage is:",percentage,"%")
if total_marks<=90:
    print("Grade=A")
elif 80<=total_marks<=89:
    print("Grade=B")
elif 70<=total_marks<=79:
    print("Grade=C")
elif 60<=total_marks<=69:
    print("Grade=D")
elif 50<=total_marks<=59:
    print("Grade=E")
else:
    print("Grade=F")

if (percentage<=50):
    print("Status:Failed")
if (percentage>=90):
    print("Status:Passed")
if (percentage>100):
    print("INVALID PERCENTAGE")
if (total_marks>500):
    print("INVALID ENTRY FOR TOTAL MARKS")


