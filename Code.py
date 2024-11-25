import random
from tkinter import *

def get_answer():
    random_number = random.randint(1,9)
    if random_number == 1:
        return 'Yes - definitely'
    elif random_number == 2:
        return 'It is decidedly so'
    elif random_number == 3:
        return 'Without a doubt'
    elif random_number == 4:
        return 'Reply hazy, try again'
    elif random_number == 5:
        return 'Ask again later'
    elif random_number == 6:
        return 'Better not tell you now'
    elif random_number == 7:
        return 'My sources say no'
    elif random_number == 8:
        return 'Outlook not so good'
    elif random_number == 9:
        return 'Very doubtful'
    else:
        return 'Error'


def ask_question():
    question = question_entry.get()
    if not question:
        answer_label.config(text="You must ask a question!")
    else:
        answer = get_answer()
        answer_label.config(text=answer)



window = Tk()
window.title("Magic 8-Ball")

# Create the GUI elements
question_label = Label(window, text="Ask your question:")
question_entry = Entry(window)
ask_button = Button(window, text="Ask", command=ask_question)
answer_label = Label(window, text="")

# Layout the elements
question_label.pack()
question_entry.pack()
ask_button.pack()
answer_label.pack()

# Start the event loop
window.mainloop()