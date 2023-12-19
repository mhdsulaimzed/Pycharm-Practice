list1="1,45rr,+"

def do(input):

    stack=[]

    s=input.split(",")

   

    

    for i in s:
        if i not in "1234567890-+%*/":
            print(i)
            return False
            break


        elif i =="+":
            op1=stack.pop()
            op2=stack.pop()

            if i =="+":
                stack.append(op1+op2)
            




        else:
            stack.append(int(i))
    return stack.pop()

print(do(list1))

