shopping_list = []

def add(item):
    shopping_list.push(item)

def remove():
    shopping_list.

def display():
    pass

def ui():
    while True:
        print("[ OPTIONS ]
               | add |
               | sub |
               | mul |
               | div |


sigTerm = False
userInput = input("Add, Remove, or Display shopping items. Press 'exit' to cancel.")

while (sigTerm):
    if userInput.toLowerCase() == 'exit':
        sigTerm = True

