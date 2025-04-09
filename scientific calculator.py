from tkinter import *
import tkinter.messagebox as tmsg
import time
import math

# Custom math functions to use degrees
math_funcs = {
    'sin': lambda x: math.sin(math.radians(x)),
    'cos': lambda x: math.cos(math.radians(x)),
    'tan': lambda x: math.tan(math.radians(x)),
    'sinh': lambda x: math.sinh(math.radians(x)),
    'cosh': lambda x: math.cosh(math.radians(x)),
    'tanh': lambda x: math.tanh(math.radians(x)),
    'log': math.log,
    'log10': math.log10,
    'exp': math.exp,
    'sqrt': math.sqrt,
    'π': math.pi,
    'e': math.e,

}

def getvals(event):
    value = event.widget.cget('text')
    if value == 'clr':
        sc_variable.set('')
    elif value == '⌫':
        current = sc_variable.get()
        sc_variable.set(current[:-1])
    elif value == '=':
        try:
            expression = screen.get()
            result = eval(expression, {"__builtins__": None}, math_funcs)
            if isinstance(result, float):
                result = round(result, 4)
            sc_variable.set(result)
        except Exception as e:
            sc_variable.set('Error - Wait 3 sec')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(3)
            sc_variable.set('')
            screen.update()
            status_var.set('Ready...')
            screen.update()
    else:
        sc_variable.set(f'{sc_variable.get()}{value}')

root = Tk()
canvas_width = 555
canvas_height = 620
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width, canvas_height)
root.minsize(canvas_width, canvas_height)
root.title('Calculator')

my_menu = Menu(root)
m1 = Menu(my_menu, tearoff=0, fg='blue')
root.config(menu=my_menu)
my_menu.add_cascade(label='About', menu=m1)
my_menu.add_command(label='Exit', command=quit)

sc_variable = StringVar()
screen = Entry(root, textvariable=sc_variable, font='lucida 35 bold', fg='black', bg='honeydew', borderwidth=10)
screen.pack(pady=30)

buttons_list = [
    ['7', '8', '9', '*', 'sin', '('],
    ['4', '5', '6', '-', 'cos', ')'],
    ['1', '2', '3', '+', 'tan', '%'],
    ['.', '0', 'sinh', 'cosh', 'tanh', 'π'],
    ['log10', 'exp', '/', 'clr', 'log', '='],
    ['⌫']
]

for row_values in buttons_list:
    f = Frame(root)
    f.pack()
    for value in row_values:
        color = 'grey' if value.isdigit() else 'grey'
        if value in ['clr']:
            color = 'blue'
        elif value in ['=' , '⌫']:
            color = 'blue'
        elif value in ['sin']:
            color = 'yellow'
        elif value == '0':
            color = 'blue'
        elif value in ['log10', 'exp']:
            color = 'blue'

        b = Button(f, text=value, font='lucida 15 bold', padx=20, pady=20,
                   borderwidth=3, fg='white', bg=color, width=3)


        b.bind('<Button-1>', getvals)
        b.pack(side=LEFT, padx=2, pady=2)

status_var = StringVar()
status_var.set('Ready...')


root.mainloop()
