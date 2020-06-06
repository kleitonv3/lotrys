import PySimpleGUI as sg

# sg.theme("DarkPurple2")

# Default cofigurations
bo = {"size":(7, 2), "font":("Franklin Gothic Book", 13), "pad":(2, 2), "button_color":("white", "#EE6352")}
bn = {"size":(7, 2), "font":("Franklin Gothic Book", 13), "pad":(2, 2), "button_color":("white", "#3FA7D6")}
be = {"size":(15, 2), "font":("Franklin Gothic Book", 13), "pad":(2, 2), "button_color":("black", "#FAC05E")}
output_screen = {"size":(14, 1), "font":("Calculator", 37), "text_color":("black"), "background_color":("#F79D84"), "pad":(4, 1), "justification":("right"), "relief":("sunken")}

layout = [  [sg.Text("Tipo atual da Calculadora", visible=False, key="_placeholder")],
			[sg.Text("Error", **output_screen, key="_screen")],
			[	sg.Button("C", **bo, key="_clear"), 
				sg.Button("CE", **bo, key="_clearLast"), 
				sg.Button("%", **bo, key="_percentage"), 
				sg.Button("÷", **bo, key="_divide")  ], 

			[	sg.Button("7", **bn, key="_num7"), 
				sg.Button("8", **bn, key="_num8"), 
				sg.Button("9", **bn, key="_num9"), 
				sg.Button("×", **bo, key="_multiply")  ],

			[	sg.Button("4", **bn, key="_num4"), 
				sg.Button("5", **bn, key="_num5"), 
				sg.Button("6", **bn, key="_num6"), 
				sg.Button("−", **bo, key="_subtract")  ],

			[	sg.Button("1", **bn, key="_num1"), 
				sg.Button("2", **bn, key="_num2"), 
				sg.Button("3", **bn, key="_num3"), 
				sg.Button("+", **bo, key="_add")  ],

			[	sg.Button(".", **bn, key="_dot"), 
				sg.Button("0", **bn, key="_num0"), 
				sg.Button("=", **be, key="_equal")  ]  ]

window = sg.Window("Calculadora", layout, margins=(1, 1), background_color=("#59CD90"), use_default_focus=False)

while True:
	event, values = window.read()

	if event in [None, 'Cancel']:
		break

window.close()