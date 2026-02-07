
def mini_calculator(num1, num2, op):
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    elif op == "mult":
        return num1 * num2
    elif op == "div":
        return num1 / num2 
    


question = input("What is the first number?")




    
result = mini_calculator(40, 7, "add")

if result == 47:
    print("MEHANEM THE BEST YES")
else: 
    print(result)



    



print(mini_calculator(1, 2, "add"))
