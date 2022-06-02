import random
from tkinter import *
from tkinter.font import Font


### Rhythm

def generate_rhythm (label):
    pattern_rhythm = ""
    
    for eight_note in range(8):
        random_number = random.randint(1,2)
        if random_number == 1:
            pattern_rhythm += " __  "
        elif eight_note % 2 == 0:
            pattern_rhythm += "DOWN "
        else:
            pattern_rhythm += " UP  "
    
    label.config(text= pattern_rhythm)


### Window configuration

window = Tk()
window.title("Random Guitar Rhythm Generator")
window.geometry("1280x720")
window.minsize(720, 480)
window.iconbitmap("re_logo2.ico")
window.config(background="#FFF7F6")


### Add elements to the window

## Frame

frame_text = Frame(window, bg = "#FFF7F6", bd= 1)

## TEXT
label_title = Label(frame_text, text = "Welcome to RGRG", font=("Helvetica", 42), bg = "#FFF7F6")
label_subtitle = Label(frame_text, text = "Click on the button to generate a rhythm pattern", font=("Helvetica", 25), bg = "#FFF7F6" )
label_rhythm_pattern = Label(window, font=("Helvetica", 25), bg = "#FFF7F6" )

## BUTTON

generate_button = Button(window, text="LET'S GET FONKY", font=("Helvetica", 20), bg = "#000000", fg= "#FFF7F6", command= lambda :generate_rhythm(label_rhythm_pattern))


## DISPLAY

label_title.pack()
label_subtitle.pack()
frame_text.pack(expand=YES)

generate_button.pack(expand=YES)
label_rhythm_pattern.pack(expand=YES)


window.mainloop()




