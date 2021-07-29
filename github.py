def add(num,num1):
	return num+num1

def sub(val,num1):
	return (val-num1)

def mul(num,num1):
	return num*num1

def div(num,num1):
	return num/num1

def mod(num,num1):
	return num%num1
def calculator():
	opr=input("Enter operator like +,-,*,/,% ")
	if opr=='+':
		x=int(input("Enter number 1: "))
		y=int(input("Enter number 2: "))
		print("Addition: ",add(x,y))
	if opr=='-':
		x=int(input("Enter number 1: "))
		y=int(input("Enter number 2: "))
		print("Subtraction: ",sub(x,y))
	if opr=='*':
		x=int(input("Enter number 1: "))
		y=int(input("Enter number 2: "))
		print("Multiplication: ",mul(x,y))

	if opr=='/':
		x=float(input("Enter number 1: "))
		y=float(input("Enter number 2: "))
		print("Division: ",div(x,y))
	if opr=='%':
		x=int(input("Enter number 1: "))
		y=int(input("Enter number 2: "))
		print("Modulus: ",mod(x,y))

def main():
	(calculator())
if __name__=="__main__":
	main()


