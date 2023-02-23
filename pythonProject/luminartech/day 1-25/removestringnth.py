s=input("enter the string")
d=int(input("enter the term to delete"))
s2=s[:d+1]+s[d+2:]
print(s2)