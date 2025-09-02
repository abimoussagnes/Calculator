#Stack class to be used in infix to postfix conversion and postfix evaluation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def priority(op):
    match(op):
        case "(":
            return 1
        case ")":
            return 2
        case "+" | "-":
            return 3
        case "%" | "/" | "*":
            return 4
        case "^":
            return 5
        case _:
            return 0

def is_operator(char):
    return char in "+-*/%^"

def remove_spaces(expr):
    return ''.join(expr.split())

#Validate what the user types in the input field
def is_valid_expression(expression):
    try:
        if not expression or expression.isspace():
            return False
            
        expr = remove_spaces(expression)
        if not expr:
            return False
            
        length = len(expr)
        i = 0
        has_digit = False
        paren_count = 0
        last_was_operator = True
        
        while i < length:
            char = expr[i]
            
            if char.isdigit():
                has_digit = True
                last_was_operator = False
                
                while i < length and (expr[i].isdigit() or expr[i] == '.'):
                    if expr[i] == '.':
                        if i + 1 >= length or not expr[i + 1].isdigit():
                            return False
                    i += 1
                i -= 1
                
            elif char == '(':
                if i > 0 and expr[i-1].isdigit():
                    return False
                paren_count += 1
                last_was_operator = True
                
            elif char == ')':
                if last_was_operator or paren_count <= 0:
                    return False
                paren_count -= 1
                last_was_operator = False
                
            elif is_operator(char):
                if char == '-' and last_was_operator:
                    if i + 1 < length and (expr[i+1].isdigit() or expr[i+1] == '('):
                        i += 1
                        continue
                    return False
                    
                if last_was_operator:
                    return False
                last_was_operator = True
                
            else:
                return False
                
            i += 1
            
        return has_digit and paren_count == 0 and not last_was_operator
        
    except Exception:
        return False

#Convert input infix expression to postfix expression
def infix_to_postfix(expression: str) -> str:
    s = ""
    res = ""
    stack = Stack()
    i = 0
    length = len(expression)
    
    while i < length:

        is_negative_start = (expression[i] == '-' and
                            i + 1 < length and
                            expression[i+1].isdigit() and
                            (i == 0 or expression[i-1] in "+-/*^("))

        if expression[i].isdigit() or is_negative_start:
            s = ""
            # Handle negative sign
            if is_negative_start:
                s += '-'
                i += 1
            # Collect all digits and decimal point
            while i < length and (expression[i].isdigit() or expression[i] == '.'):
                s += expression[i]
                i += 1
            res += s + " "
            i -= 1
            
        elif expression[i] in "+-/%*^()":
            if expression[i] == '(':
                stack.push(expression[i])
            elif expression[i] == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    res += stack.pop() + " "
                if not stack.is_empty():
                    stack.pop()
            else:
                while (not stack.is_empty() and
                        stack.peek() != '(' and
                        priority(stack.peek()) >= priority(expression[i])):
                    res += stack.pop() + " "
                stack.push(expression[i])
        i += 1

    while not stack.is_empty():
        op = stack.pop()
        if op != '(':
            res += op + " "

    return res.strip()

#Convert postfix expression to its value
def postfix_eval(expression: str):
    s = ""
    stack = Stack()
    length = len(expression)
    i = 0

    while i < length:
        # Skip spaces
        if expression[i].isspace():
            i += 1
            continue
            
        # Handle numbers (including negative numbers)
        if expression[i].isdigit() or (expression[i] == '-' and i + 1 < length and expression[i+1].isdigit()):
            s = ""
            if expression[i] == '-':
                s += '-'
                i += 1
            # Collect digits and decimal point
            while i < length and (expression[i].isdigit() or expression[i] == '.'):
                s += expression[i]
                i += 1
            # Convert to float and push to stack
            if s:
                stack.push(float(s))
            continue
            
        # Handle operators
        elif is_operator(expression[i]):
            if len(stack.items) < 2:
                raise ValueError("Invalid expression: not enough operands")
            a = stack.pop()
            b = stack.pop()
            
            match expression[i]:
                case "+":
                    stack.push(b + a)
                case "-":
                    stack.push(b - a)
                case "*":
                    stack.push(b * a)
                case "/":
                    if a == 0:
                        raise ZeroDivisionError("Division by zero")
                    stack.push(b / a)
                case "%":
                    if a == 0:
                        raise ValueError("Modulo by zero")
                    stack.push(b % a)
                case "^":
                    stack.push(b ** a)
        i += 1

    # Check final stack state
    if stack.is_empty():
        raise ValueError("Invalid expression: empty result")
    result = stack.pop()
    if not stack.is_empty():
        raise ValueError("Invalid expression: too many operands")
        
    return int(result) if result % 1 == 0 else result

def evaluate(expression: str):
    if is_valid_expression(expression):
            postfix = infix_to_postfix(remove_spaces(expression))
            return postfix_eval(postfix)
    else:
        raise ValueError("Invalid input")