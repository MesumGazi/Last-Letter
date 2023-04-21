import PySimpleGUI as sg

def get_first_word():
    first_layout = [    
        [sg.T("Enter the first word:")],
        [sg.I(key="-first_word-")],
        [sg.Button("OK")]
    ]

    first_window = sg.Window("Word Chain Game - First Word", first_layout)

    event, values = first_window.read()
    if event == sg.WIN_CLOSED:
        exit()

    first_word = values["-first_word-"]
    ending_letter = first_word[-1]
    first_window.close()

    return first_word, ending_letter

score_count = 0

first_word, ending_letter = get_first_word()

subsequent_layout = [    
    [sg.T(f"Enter a word starting with '{ending_letter}':")],
    [sg.I(key="-subsequent_word-")],
    [sg.Button("OK")]
]

while True:
    subsequent_window = sg.Window("Word Chain Game - Word starting with '{}'".format(ending_letter), subsequent_layout)

    event, values = subsequent_window.read()
    if event == sg.WIN_CLOSED:
        break

    subsequent_word = values["-subsequent_word-"]
    score_count += 1

    if subsequent_word[0] != ending_letter:
        sg.popup("The word should start with '{}'".format(ending_letter))
        sg.popup("YOU LOSE!", f"Score: {score_count}")
        break

    ending_letter = subsequent_word[-1]

    subsequent_layout = [
        [sg.T(f"Enter a word starting with '{ending_letter}':")],
        [sg.I(key="-subsequent_word-")],
        [sg.Button("OK")]
    ]

    subsequent_window.close()

    print(subsequent_word)

sg.popup("Game over")
