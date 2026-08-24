# n=int(input("Enter a number:"))

# for n in range(1,20):
#    if n % 2 != 0:
#     print(n)

# num=int(input("Enter a number:"))
# for i in range(1,11):
#  result=num*i
#  print(result)
 
# num=int(input("Enter a number:"))
# for num in range(1,51):
#     if num % 3 == 0:
#      if num==15:
#         continue
#     print(num)

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
for i in range(1,10001):
 if i % a == 0: if i % b==0:
 print("First no:",i)
 break
else:
  print("No number is divisible by both")
