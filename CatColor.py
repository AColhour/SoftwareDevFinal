"""
This program is a personality quiz that tells you what color your fur
would be if you were a cat.
By Alexandria Colhour
It is a combination of 9 questions in which the user ranks themselves
from 1 to 7, each button of each question correlating with a color
key in a dictionary. When the user presses a button, the correlating
color increases by 1. At the end, the max value will display as the
user's 'result'.
"""

import operator
from tkinter import *

window = Tk()  # establishes the window
window.title("Cat Color")  # adds the title to the window
window.configure(bg='lightpink')  # makes the background of the window pink
frame = Frame(window)  # creates a frame
frame.grid(row=0, column=0)  # establishes a grid on the frame

"""
color declarations
declares the dictionary and
sets each color to 0 in the dictionary to begin
"""

color = {
    'orange':0,
    'white':0,
    'black':0,
    'gray':0,
    'bicolor':0,
    'tricolor':0,
    'tabby':0
}

"""
color increments
used to += 1 to each color when called by button
"""

def orangeinc():
    color['orange'] += 1

def whiteinc():
    color['white'] += 1

def blackinc():
    color['black'] += 1

def grayinc():
    color['gray'] += 1

def bicolorinc():
    color['bicolor'] += 1

def tricolorinc():
    color['tricolor'] += 1

def tabbyinc():
    color['tabby'] += 1



"""
First question label 
"""
label = Label(frame, bg= 'lightpink', text="With 1 being intolerant and 7 being tolerant, where would you rank yourself?")
label.config(font=("Arial", 10))
label.grid(row=0, column=0, columnspan=21)




"""
Q2 buttons and question
"""
def q2():
    label["text"] = "With 1 being nosy and 7 being aloof, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [orangeinc(), q3()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [whiteinc(), q3()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [tabbyinc(), q3()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [tricolorinc(), q3()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [bicolorinc(), q3()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [blackinc(), q3()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [grayinc(), q3()])
    button.grid(row=1, column=6)





"""
Q3 buttons and question
"""
def q3():
    label["text"] = "With 1 being docile and 7 being stubborn, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [blackinc(), q4()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [orangeinc(), q4()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [tabbyinc(), q4()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [grayinc(), q4()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [whiteinc(), q4()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [bicolorinc(), q4()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [tricolorinc(), q4()])
    button.grid(row=1, column=6)





"""
Q4 buttons and question
"""

def q4():
    label["text"] = "With 1 being hyper and 7 being calm, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [tricolorinc(), q5()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [blackinc(), q5()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [whiteinc(), q5()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [tabbyinc(), q5()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [bicolorinc(), q5()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [grayinc(), q5()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [orangeinc(), q5()])
    button.grid(row=1, column=6)





"""
Q5 buttons and question
"""
def q5():
    label["text"] = "With 1 being outgoing and 7 being shy, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [blackinc(), q6()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [whiteinc(), q6()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [tricolorinc(), q6()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [tabbyinc(), q6()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [orangeinc(), q6()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [bicolorinc(), q6()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [grayinc(), q6()])
    button.grid(row=1, column=6)




"""
Q6 buttons and question
"""
def q6():
    label["text"] = "With 1 being unfriendly and 7 being friendly, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [grayinc(), q7()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [tricolorinc(), q7()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [blackinc(), q7()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [whiteinc(), q7()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [bicolorinc(), q7()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [tabbyinc(), q7()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [orangeinc(), q7()])
    button.grid(row=1, column=6)





"""
Q7 buttons and question
"""
def q7():
    label["text"] = "With 1 being untrainable and 7 being trainable, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [grayinc(), q8()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [blackinc(), q8()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [whiteinc(), q8()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [tricolorinc(), q8()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [bicolorinc(), q8()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [tabbyinc(), q8()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [orangeinc(), q8()])
    button.grid(row=1, column=6)





"""
Q8 buttons and question
"""
def q8():
    label["text"] = "With 1 being undaring and 7 being bold, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [blackinc(), q9()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [bicolorinc(), q9()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [tricolorinc(), q9()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [whiteinc(), q9()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [grayinc(), q9()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [orangeinc(), q9()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [tabbyinc(), q9()])
    button.grid(row=1, column=6)



"""
Q9 buttons and question
"""
def q9():
    label["text"] = "With 1 being lazy and 7 being active, where would you rank yourself?"
    buttonFrame = Frame(window)
    buttonFrame.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 1 ', command= lambda: [blackinc(), end()])
    button.grid(row=1, column=0)

    button = Button(buttonFrame, text=' 2 ', command= lambda: [grayinc(), end()])
    button.grid(row=1, column=1)

    button = Button(buttonFrame, text=' 3 ', command= lambda: [whiteinc(), end()])
    button.grid(row=1, column=2)

    button = Button(buttonFrame, text=' 4 ', command= lambda: [orangeinc(), end()])
    button.grid(row=1, column=3)

    button = Button(buttonFrame, text=' 5 ', command= lambda: [bicolorinc(), end()])
    button.grid(row=1, column=4)

    button = Button(buttonFrame, text=' 6 ', command= lambda: [tricolorinc(), end()])
    button.grid(row=1, column=5)

    button = Button(buttonFrame, text=' 7 ', command= lambda: [tabbyinc(), end()])
    button.grid(row=1, column=6)




"""
establish result window and display result-specific picture
"""
def open_Toplevel1():

    top1 = Toplevel(window)
    top1.title('Results')
    resultlabel = Label(top1, text='You would have '+ colormax + ' fur!')
    resultlabel.grid(row=0, column=0)
    resultlabel.configure(font=("Arial", 20))
    button = Button(top1, text='Quit', command= close)
    button.grid(row=0, column=2)

    if colormax == 'orange':
        img = PhotoImage(file='orangecat.png')
        imglabel = Label(top1, image=img)
        imglabel.grid(row=1, column=0)
        top1.mainloop()
    if colormax == 'tabby':
        img = PhotoImage(file='tabbycat.png')
        imglabel = Label(top1, image=img)
        imglabel.grid(row=1, column=0)
        top1.mainloop()
    if colormax == 'bicolor':
        img = PhotoImage(file='bicolorcat.png')
        imglabel = Label(top1, image=img)
        imglabel.grid(row=1, column=0)
        top1.mainloop()
    if colormax == 'black':
        img = PhotoImage(file='blackcat.png')
        imglabel = Label(top1, image=img)
        imglabel.grid(row=1, column=0)
        top1.mainloop()
    if colormax == 'white':
        img = PhotoImage(file='whitecat.png')
        imglabel = Label(top1, image=img)
        imglabel.grid(row=1, column=0)
        top1.mainloop()
    if colormax == 'tricolor':
        img = PhotoImage(file='tricolorcat.png')
        imglabel = Label(top1, image=img)
        imglabel.grid(row=1, column=0)
        top1.mainloop()
    if colormax == 'gray':
        img = PhotoImage(file='graycat.png')
        imglabel = Label(top1, image=img)
        imglabel.grid(row=1, column=0)
        top1.mainloop()







"""
determine which color had the max 
"""
def colorchooser():
    global colormax
    colormax = max(color.items(), key=operator.itemgetter(1))[0]



"""
open top level and run colorchooser to determine which color had the max
"""
def end():
    label.destroy()
    button.destroy()
    colorchooser()
    open_Toplevel1()


"""
exit button function
"""
def close():
    window.destroy()



"""
Q1 buttons
"""

buttonFrame = Frame(window)
buttonFrame.grid(row=1, column=0)

button = Button(buttonFrame, text=' 1 ', command= lambda: [orangeinc(),q2()])
button.grid(row=1, column=0)

button = Button(buttonFrame, text=' 2 ', command= lambda: [tabbyinc(),q2()])
button.grid(row=1, column=1)

button = Button(buttonFrame, text=' 3 ', command= lambda: [bicolorinc(),q2()])
button.grid(row=1, column=2)

button = Button(buttonFrame, text=' 4 ', command= lambda: [blackinc(),q2()])
button.grid(row=1, column=3)

button = Button(buttonFrame, text=' 5 ', command= lambda: [whiteinc(),q2()])
button.grid(row=1, column=4)

button = Button(buttonFrame, text=' 6 ', command= lambda: [tricolorinc(),q2()])
button.grid(row=1, column=5)

button = Button(buttonFrame, text=' 7 ', command= lambda: [grayinc(),q2()])
button.grid(row=1, column=6)

button = Button(text='Quit', command= close)
button.grid(row=1, column=12)







window.mainloop()