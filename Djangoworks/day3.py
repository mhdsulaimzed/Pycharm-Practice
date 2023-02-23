# n=10
# print("posative" if n>0 else "neg")
#
# n=200
# n2=500
# print(" n is greater" if n>n2 else n2>n,"n2 is greater" )
# def smart_sub(n1,n2):
#     return n

# smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
# print(smart_sub(20,15))
# odd_check=lambda n:"even" if n%2==0 else "odd"
# print(odd_check(10))

x=lambda a: a+10
print(x(5))

def myfun(n):
    return lambda a: a * n
mydoub=myfun(3)
mytrip=myfun(2)
print(mydoub(11))
print(mytrip(11))
