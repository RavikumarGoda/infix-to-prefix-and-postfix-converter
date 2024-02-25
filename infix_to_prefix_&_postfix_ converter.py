from tkinter import *

MAX = 100
st = [0] * MAX

def infixtopostfix(temp):
    postfix = ""
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    for char in temp:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '(' from the stack
        else:
            while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix

def convert():
    infix_expression = infix_entry.get()
    postfix_expression = infixtopostfix(infix_expression)
    reverse_expression = infixtopostfix(infix_expression[::-1])[::-1]
    postfix_label.config(text="Postfix Expression: " + postfix_expression)
    prefix_label.config(text="Prefix Expression: " + reverse_expression)

root = Tk()
root.geometry("400x200")
root.title("Infix to Postfix/Prefix Converter")

infix_label = Label(root, text="Enter an infix expression:")
infix_label.pack()

infix_entry = Entry(root, width=50)
infix_entry.pack()

convert_button = Button(root, text="Convert", command=convert)
convert_button.pack()

postfix_label = Label(root, text="")
postfix_label.pack()

prefix_label = Label(root, text="")
prefix_label.pack()

root.mainloop()
