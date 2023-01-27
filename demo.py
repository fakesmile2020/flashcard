import tkinter as tk
import pandas as pd
import random

# read excel file
flashcard_data = pd.read_excel("flashcards.xlsx")


# create a list of flashcards from the data
flashcards = [ (row['question'], row['answer']) for index, row in flashcard_data.iterrows()]

# shuffle flashcards 
random.shuffle(flashcards)

class FlashCardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flash Card Application")
        self.geometry("800x600")
        self.flashcards = flashcards
        self.current_flashcard = 0
        self.score = 0
        self.score_label = tk.Label(self, text="Score: 0")
        self.score_label.grid(row=0,column=0)
        self.time_left = 30
        self.time_label = tk.Label(self, text="Time left: 30")
        self.time_label.grid(row=1,column=0)
        self.question_label = tk.Label(self, text=self.flashcards[self.current_flashcard][0])
        self.question_label.grid(row=2,column=0,sticky='nsew')
        self.question_label.config(font=("Arial", 20))
        self.answer_input = tk.Entry(self)
        self.answer_input.grid(row=3,column=0,sticky='nsew')
        self.answer_input.config(font=("Arial", 20))
        self.answer_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.answer_button.grid(row=4,column=0)
        self.result_label = tk.Label(self, text=" ")
        self.result_label.grid(row=5,column=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.score_label.config(font=("Arial", 20))
        self.time_label.config(font=("Arial", 20))
        self.start_timer()

    def start_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text ="Time left: " + str(self.time_left))
            self.after(1000, self.start_timer)
        else:
            self.time_label.config(text="Time's up!")
            self.answer_input.config(state='disable')

    def check_answer(self): 
        answer = self.answer_input.get()
        if answer == self.flashcards[self.current_flashcard][1]:
            self.result_label.config(text="Correct!")
            self.score += 1
            self.score_label.config(text="Score: "+str(self.score))
        else:
            self.result_label.config(text="Incorrect. The correct answer is: "+self.flashcards[self.current_flashcard][1])
        self.current_flashcard = (self.current_flashcard + 1) % len(self.flashcards)
        self.question_label.config(text=self.flashcards[self.current_flashcard][0])
        self.answer_input.delete(0,tk.END)
            
    


if __name__ == "__main__":
    app = FlashCardApp()
    app.mainloop()
