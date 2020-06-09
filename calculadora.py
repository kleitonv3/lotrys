import PySimpleGUI as sg

# Defining operations to the calculator

def clearScreen ():
	window['screen'].update("")

def insertNum (val):
	aux = window['screen'].Get()
	if aux in ['0', '÷', '×', '−', '+']:
		aux = ""
	clearScreen()
	window['screen'].update(aux+val)

def insertOperation (op):
	global first_num
	first_num = window['screen'].Get()
	global op_atual
	op_atual = op
	window['screen'].update(op)
	return first_num, op_atual

def result ():
	last_num = window['screen'].Get()
	try:
		if op_atual == "÷":
			res = int(first_num)/int(last_num)
		if op_atual == "×":
			res = int(first_num)*int(last_num)
		if op_atual == "−":
			res = int(first_num)-int(last_num)
		if op_atual == "+":
			res = int(first_num)+int(last_num)

		window['screen'].update(str(res))
	except:
		window['screen'].update("Error")

# sg.theme("DarkPurple2")

# Default cofigurations
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

layout = [  [sg.Text("Tipo atual da Calculadora", visible=False, key="placeholder")],
			[sg.Text("0", **screen, key="screen")],
			[	sg.Button("C", **bo, key="clear"), 
				sg.Button("CE", **bo, key="clearLast"), 
				sg.Button("%", **bo, key="percentage"), 
				sg.Button("÷", **bo, key="divide")  ], 

			[	sg.Button("7", **bn, key="num7"), 
				sg.Button("8", **bn, key="num8"), 
				sg.Button("9", **bn, key="num9"), 
				sg.Button("×", **bo, key="multiply")  ],

			[	sg.Button("4", **bn, key="num4"), 
				sg.Button("5", **bn, key="num5"), 
				sg.Button("6", **bn, key="num6"), 
				sg.Button("−", **bo, key="subtract")  ],

			[	sg.Button("1", **bn, key="num1"), 
				sg.Button("2", **bn, key="num2"), 
				sg.Button("3", **bn, key="num3"), 
				sg.Button("+", **bo, key="add")  ],

			[	sg.Button(".", **bn, key="dot"), 
				sg.Button("0", **bn, key="num0"), 
				sg.Button("=", **be, key="equal")  ]  ]

window = sg.Window("Calculadora", layout, margins=(1, 1), background_color=("#59CD90"), use_default_focus=False)

while True:
	event, values = window.read()

	if event in [None, 'Cancel']:
		break
	if event in ['num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9']:
		insertNum(event[-1])
	if event == 'percentage':
		clearScreen() # Need implementation
	if event == 'divide':
		insertOperation("÷")
	if event == 'multiply':
		insertOperation("×")
	if event == 'subtract':
		insertOperation("−")
	if event == 'add':
		insertOperation("+")
	if event == 'equal':
		result()
	if event in ['clear', 'clearLast']:
		first_num = op_atual = ""
		clearScreen()
		window['screen'].update("0")

window.close()
