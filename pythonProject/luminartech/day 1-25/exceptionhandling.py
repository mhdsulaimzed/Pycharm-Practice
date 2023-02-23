#EXCEPTION HANDLING

#TRY , EXCEPT, FINALLY,ELSE
try:
     a=int(input("entyer the first number"))
     b=int(input("enetr the second number"))
     div=a/b
     print(div)
except ZeroDivisionError:
    print("enter the secont number non zero")
except ValueError:
    print("plz enter a valid number")