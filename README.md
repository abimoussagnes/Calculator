# Calculator Application

A fully functional calculator implemented in Python using the Tkinter library for the graphical user interface. This calculator supports complex mathematical expressions with operator precedence and parentheses.

## Features

- Basic arithmetic operations (+, -, *, /)
- Advanced operations (%, ^)
- Support for decimal numbers
- Support for negative numbers
- Parentheses for expression grouping
- Mathematical constant π (pi)
- Clear function (C)
- Error handling for invalid expressions

## Technologies Used

- Python 3.x
- Tkinter (GUI library)
- Custom Stack implementation
- Infix to Postfix conversion algorithm

## How It Works

1. **Expression Parsing**: Uses a custom algorithm to validate mathematical expressions
2. **Infix to Postfix Conversion**: Converts regular mathematical notation to postfix notation using stack data structure
3. **Postfix Evaluation**: Evaluates the postfix expression to calculate the final result

## Implementation Details

### Core Components

- `calculator.py`: Main GUI implementation using Tkinter
- `util.py`: Contains core functionality:
  - Stack implementation
  - Expression validation
  - Infix to postfix conversion
  - Postfix evaluation

### Key Algorithms

1. **Expression Validation**
   - Checks for valid number formats
   - Validates operator placement
   - Ensures balanced parentheses
   - Handles negative numbers

2. **Infix to Postfix Conversion**
   - Uses operator precedence
   - Handles parentheses
   - Preserves number formatting
   - Supports negative numbers

3. **Expression Evaluation**
   - Stack-based evaluation
   - Error handling for division by zero
   - Support for decimal and integer results

## Usage

1. Run `calculator.py` to start the application
2. Enter mathematical expressions using:
   - Number buttons (0-9)
   - Operator buttons (+, -, *, /, %, ^)
   - Decimal point (.)
   - Parentheses ( )
3. Press '=' to evaluate
4. Press 'C' to clear

## Examples

```
Basic: 3 + 5 = 8
Decimal: 10.5 / 2 = 5.25
Negative: -3 * 4 = -12
Complex: (2 + 3) * 4 = 20
Power: 2 ^ 3 = 8
With π: π * 2 = 6.28318...
```

## Error Handling

- Division by zero
- Invalid expressions
- Unmatched parentheses
- Consecutive operators
- Invalid number formats

## Future Improvements

- Scientific calculator functions
- Memory functions
- History of calculations
- Keyboard input support
- Additional mathematical constants

## Project Structure

```
Calculator/
│
├── calculator.py    # Main GUI application
├── util.py         # Core calculator logic
└── README.md       # Documentation
```

## Learning Outcomes

This project demonstrates:
- Stack data structure implementation
- Expression parsing and validation
- Algorithm design for mathematical operations
- GUI development with Tkinter
- Error handling and input validation
