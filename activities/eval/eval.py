"""Evaluate an expression of the type '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'."""

import sys
from array_stack import ArrayStack

def main():
    ops = ArrayStack()
    values = ArrayStack()

    tokens = sys.stdin.readline().split()  # read a single of input and split around whitespaces
    n = len(tokens)
    for i in range(n):
        token = tokens[i]
        if   token == '+': ops.push(token)
        elif token == '-': ops.push(token)
        elif token == '*': ops.push(token)
        elif token == ')':
            op = ops.pop()
            value = values.pop()
            if   op == '+':   value = values.pop() + value
            if   op == '-':   value = values.pop() - value
            if   op == '*':   value = values.pop() * value
            values.push(value)
        elif token != '(':
            values.push(int(token))
    print(str(values.pop()))

if __name__ == '__main__':
    main()
