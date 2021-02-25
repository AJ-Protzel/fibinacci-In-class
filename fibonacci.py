# def fibonacci(n, x, y):
#   if(n == 1):
#     return x
#   else:
#     return fibonacci(n-1, y, x+y)

def fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    # if n < 0:
    #     print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    if(n == 0):
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif(n == 1 or n == 2):
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)