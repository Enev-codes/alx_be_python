def add(num1: float, num2: float) -> float:
    return num1 + num2

def sub(num1: float, num2: float) -> float:
    return num1 - num2

def mul(num1: float, num2: float) -> float:
    return num1 * num2

def div(num1: float, num2: float) -> float:
    return num1 / num2

def perform_operation(num1: float, num2: float, operation: str) -> float:
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
