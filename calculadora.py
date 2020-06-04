import PySimpleGUI as sg

# sg.theme("DarkPurple2")

# Default cofigurations
bo = {"size":(7, 2), "font":("Franklin Gothic Book", 13), "pad":(2, 2), "button_color":("white", "#EE6352")}
bn = {"size":(7, 2), "font":("Franklin Gothic Book", 13), "pad":(2, 2), "button_color":("white", "#3FA7D6")}
be = {"size":(15, 2), "font":("Franklin Gothic Book", 13), "pad":(2, 2), "button_color":("black", "#FAC05E")}
output_screen = {"size":(14, 1), "font":("Calculator", 37), "text_color":("black"), "background_color":("#F79D84"), "pad":(4, 1), "justification":("right"), "relief":("sunken")}

layout = [  [sg.Text("Tipo atual da Calculadora", visible=False)],
			[sg.Text("Error", **output_screen)],
			[sg.Button("C", **bo), sg.Button("CE", **bo), sg.Button("%", **bo), sg.Button("÷", **bo)  ],  
			[sg.Button("7", **bn), sg.Button("8", **bn), sg.Button("9", **bn), sg.Button("×", **bo)  ],
			[sg.Button("4", **bn), sg.Button("5", **bn), sg.Button("6", **bn), sg.Button("−", **bo)  ],
			[sg.Button("1", **bn), sg.Button("2", **bn), sg.Button("3", **bn), sg.Button("+", **bo)  ],
			[sg.Button(",", **bn), sg.Button("0", **bn), sg.Button("=", **be)  ]  ]

window = sg.Window("Calculadora", layout, margins=(1, 1), background_color=("#59CD90"), use_default_focus=False)

while True:
	event, values = window.read()

	if event in [None, 'Cancel']:
		break

window.close()