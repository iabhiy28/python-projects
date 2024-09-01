#Calculator

def sum(num1 , num2):
    return num1 + num2


def sub(num1 , num2):
    return num1 - num2


def mul(num1 , num2):
    return num1 * num2

def div(num1 , num2):
    return num1/num2

operations = {
    "+":sum,
    "-":sub,
    "*":mul,
    "/":div
}
num1 = int(input("Enter the first oerand:"))
num2 = int(input("Enter the second operand"))

for symbol in operations:
    print(symbol)

choice = input("Enter the above Operation:")

function_calling = operations[choice]
answer = function_calling(num1 , num2)

print(f"{num1} {choice} {num2} = {answer}")


