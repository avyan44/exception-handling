try:
    num1,num2=eval(input("enter two numbers, seperated by a comma :"))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is error!!")
except SyntaxError:
    print("comma is missing.Enter numbers separated by comma like this 1,1")    
except:
    print("wrong input")
finally:
    print("this will exacute no matter what")    
        