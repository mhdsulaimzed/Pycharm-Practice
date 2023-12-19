def evaluate(string):
    stack=[]
    for i in string:
       
       
        if i not in "1234567890-+%*/":
            
            stack.append("undefined")
            break


        if i in ["+","-","*","/","%"]:
            opr1=stack.pop()
            opr2=stack.pop()

            if i == "+":
                stack.append(opr1+opr2)

            elif i == "-":
                stack.append(opr2-opr1)

            elif i == "*":
                stack.append(opr1*opr2) 
            

            elif i == "/" and opr1>0:
                stack.append(opr2//opr1)

            elif i == "/" and opr1==0:
                 try:
                    stack.append(opr2//opr1)

                 except ZeroDivisionError as e:
                     stack.append("undefined")

            
                

            elif i == "%" and opr1>0:
                stack.append(opr2%opr1)

            elif i == "%" and opr1==0:
                 try:
                    stack.append(opr2%opr1)

                 except ZeroDivisionError as e:
                     stack.append("undefined")

print(evaluate("5+")



        else:    
            stack.append(int(i))

    return stack.pop()
print(evaluate("5h+"))









