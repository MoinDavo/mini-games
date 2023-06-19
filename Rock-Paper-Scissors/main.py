import tkinter
from tkinter import ttk
import random

CHOICES = ["Rock", "Paper", "Scissors"]

# init tkinter/ttk
root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# add labels
label_1 = tkinter.Label(frm, text= "your Choice:")
label_1.grid(column=0, row=1)

user_choice_label = tkinter.Label(frm, text= "")
user_choice_label.grid(column=0, row=2)

label_2 = tkinter.Label(frm, text="randomiser:")
label_2.grid(column=1, row=1)

rand_choice_label = tkinter.Label(frm, text="")
rand_choice_label.grid(column=1, row=2)

label_3 = tkinter.Label(frm, text="result:")
label_3.grid(column=2, row=1)

result_label = tkinter.Label(frm, text="")
result_label.grid(column=2, row=2)

# game logic
def gameLogic(userInput):
    # randomisers
    rand_choice = random.choice(CHOICES)
    #print(rand_choice)
    rand_choice_label.config(text=rand_choice)

    if userInput == "Random":
        userInput = random.choice(CHOICES)
        #print(userInput)
    
    user_choice_label.config(text=userInput)

    match rand_choice:
           case "Rock":
                  match userInput:
                         case "Rock":
                                out = "Draw"
                                #print(out)
                                return out
                         case "Paper":
                                out = "Win"
                                #print(out)
                                return out
                         case "Scissors":
                                out = "Loose"
                                #print(out)
                                return out
                         case _:
                                out = "err: user input"
                                #print(out)
                                return out
       
           case "Paper":
                  match userInput:
                         case "Rock":
                                out = "Loose"
                                #print(out)
                                return out
                         case "Paper":
                                out = "Draw"
                                #print(out)
                                return out
                         case "Scissors":
                                out = "Win"
                                #print(out)
                                return out
                         case _:
                                out = "err: user input"
                                #print(out)
                                return out

           case "Scissors":
                  match userInput:
                         case "Rock":
                                out = "Win"
                                #print(out)
                                return out
                         case "Paper":
                                out = "Loose"
                                #print(out)
                                return out
                         case "Scissors":
                                out = "Draw"
                                #print(out)
                                return out
                         case _:
                                out = "err: user input"
                                #print(out)
                                return out
           case _:
                  out = "err: randomiser"
                  #print(out)
                  return out

# lambda expressions for buttons
def logicR():
    user_choice_label.config(text="")
    result_label.config(text=gameLogic("Rock"))

def logicP():
    user_choice_label.config(text="")
    result_label.config(text=gameLogic("Paper"))

def logicS():
    user_choice_label.config(text="")
    result_label.config(text=gameLogic("Scissors"))

def logicRand():
    user_choice_label.config(text="")
    result_label.config(text=gameLogic("Random"))

# buttons
rock_btn = ttk.Button(frm, text="Rock", command=logicR )
rock_btn.grid(column=0, row=0)

paper_btn = ttk.Button(frm, text="Paper", command=logicP )
paper_btn.grid(column=1, row=0)

scissors_btn = ttk.Button(frm, text="Scissors", command=logicS )
scissors_btn.grid(column=2, row=0)

rand_btn = tkinter.Button(frm, text="Random", command=logicRand )
rand_btn.grid(column=3, row=0)

quit_btn = ttk.Button(frm, text="quit", command=root.destroy)
quit_btn.grid(column=3, row= 2)
root.mainloop()
