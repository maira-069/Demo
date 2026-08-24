a=float(input("Enter a 1st no:"))
b=float(input("Enter a 2nd no:"))
op=str(input("Enter operator:"))
if (op=='+'):
 sum=a+b
 print("sum:",sum)
elif (op=='-'):
 sub=a-b
 print("sub:",sub)
elif (op=='*'):
  mul=a*b
  print("mul:",mul)
elif (op=='%'):
 div=a%b
 print("DIV:",div)
elif (op=='**'):
 power=a**b
 print("power:",power)
else:
 print("INVALID entry.")

