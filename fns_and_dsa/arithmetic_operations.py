def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def perform_operation(num1, num2, operation):
    oper_map = {
            'add': add,
            'subtract': sub,
            'multiply': mul,
            'divide': div
            }
    try:
        func = oper_map.get(operation)(num1, num2)
        if func:
            return func
        return None
    except:
        print("[ Error ]: Invalid operation")
