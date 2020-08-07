import PySimpleGUI as sg

# Defining operations to the calculator
def clear_screen():
	window['screen'].update("0")
	aux['result'] = None
	aux['isFloat'] = False
	aux['olderNumber'] = None
	aux['operator'] = None

def insert_number(val):
	older = window['screen'].get()
	if older == "0" and val != ".":
		# just to don't use the left zero after a clear_screen()
		older = ""
	window['screen'].update(older + str(val))

def make_operation(val):
	if aux['isFloat']:
		aux['olderNumber'] = float(window['screen'].get())
	else:
		aux['olderNumber'] = int(window['screen'].get())

	window['screen'].update("0")

def pow_operation():
	if aux['isFloat']:
		aux['result'] = float(window['screen'].get())**2
	else:
		aux['result'] = int(window['screen'].get())**2

	window['screen'].update(str(aux['result']))

def sqrt_operation():
	aux['result'] = float(window['screen'].get())**(0.5)

	window['screen'].update('{:.6f}'.format(aux['result']))

def calculate():
	if aux['isFloat']:
		actual = float(window['screen'].get())
	else:
		actual = int(window['screen'].get())

	op = aux['operator']

	if op == '+':
		aux['result'] = aux['olderNumber'] + actual
	if op == '-':
		aux['result'] = aux['olderNumber'] - actual
	if op == '*':
		aux['result'] = aux['olderNumber'] * actual
	if op == '/':
		aux['result'] = '{:.6f}'.format(aux['olderNumber'] / actual)

	window['screen'].update(str(aux['result']))


# sg.theme("DarkPurple2")

# Default configurations
bo = {	
"size":(7, 2), 
"font":("Franklin Gothic Book", 13), 
"pad":(2, 2), 
"button_color":("white", "#EE6352")  }

bn = {	
"size":(7, 2), 
"font":("Franklin Gothic Book", 13), 
"pad":(2, 2), 
"button_color":("white", "#3FA7D6")  }

be = {	
"size":(15, 2), 
"font":("Franklin Gothic Book", 13), 
"pad":(2, 2), 
"button_color":("black", "#FAC05E")  }

screen = {	
"size":(14, 1), 
"font":("Calculator", 37), 
"text_color":("black"), 
"background_color":("#F79D84"), 
"pad":(4, 1), 
"justification":("right"), 
"relief":("sunken")  }

# Defining the global variables as a list
aux = {'result': None, 'isFloat': False, 'olderNumber': None, 'operator': None}

layout = [  [sg.Text("Tipo atual da Calculadora", visible=False, key="placeholder")],
			[sg.Text("0", **screen, key="screen")],
			[	sg.Button("C", **bo, key="clear"), 
				sg.Button("x²", **bo, key="pow"), 
				sg.Button("√x", **bo, key="sqrt"), 
				sg.Button("÷", **bo, key="/")  ], 

			[	sg.Button("7", **bn, key="num7"), 
				sg.Button("8", **bn, key="num8"), 
				sg.Button("9", **bn, key="num9"), 
				sg.Button("×", **bo, key="*")  ],

			[	sg.Button("4", **bn, key="num4"), 
				sg.Button("5", **bn, key="num5"), 
				sg.Button("6", **bn, key="num6"), 
				sg.Button("−", **bo, key="-")  ],

			[	sg.Button("1", **bn, key="num1"), 
				sg.Button("2", **bn, key="num2"), 
				sg.Button("3", **bn, key="num3"), 
				sg.Button("+", **bo, key="+")  ],

			[	sg.Button(".", **bn, key="."), 
				sg.Button("0", **bn, key="num0"), 
				sg.Button("=", **be, key="=")  ]  ]

window = sg.Window("Calculadora", layout, margins=(1, 1), background_color=("#59CD90"), use_default_focus=False)

while True:
	event, values = window.read()

	if event in [None, 'Cancel']:
		break

	if event in ['clear']:
		clear_screen()

	if event in ['num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9']:
		insert_number(event[-1])

	if event in ['.']:
		aux['isFloat'] = True
		insert_number('.')

	if event in ['+', '-', '*', '/']:
		aux['operator'] = event
		make_operation(event)

	if event in ['pow']:
		pow_operation()

	if event in ['sqrt']:
		sqrt_operation()

	if event in ['=']:
		calculate()



	
	
window.close()
