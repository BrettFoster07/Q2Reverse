userinput=input("Please Input A Word")
n=0
num=""
for i in range (0,len(userinput)):
  n=n-1
  num=num+userinput[n]
print()
print("Your Word Backwords Is",num)