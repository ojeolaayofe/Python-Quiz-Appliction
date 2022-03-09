from  tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:

    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val +=1
    def check_answer(self,q_no):
        if self.opt_selected.get() ==answer[q_no]:
            return True
    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(root,text=" ", variable=self.opt_selected, value=len(q_list) + 1, font=("ariel",14))
            q_list.append(radio_btn)
            radio_btn.place(x=100,y=y_pos)
            y_pos += 40
        return q_list
    def display_question(self):
        q_no = Label(root,text=question[self.q_no], width=60,font=("ariel",16,"bold"),anchor="w")
        q_no.place(x=70,y=100)
    def display_title(self):
        title = Label(root, text="NIIT Examination Portal", width=50,bg="green",fg="white",font=("arial",20,"bold"))
        title.place(x=0,y=2)
    def next_btn(self):
        if self.check_answer(self.q_no):
            self.correct +=1
        self.q_no +=1
        if self.q_no == self.data_size:
            self.display_result()
            root.destroy()
        else:
            self.display_question()
            self.display_options()
    def display_result(self):
        wrong_count = self.data_size -self.correct
        correct = f"Your Correct answer is : {self.correct}"
        wrong = f"Your Wrong answers is :{wrong_count}"
        score = int(self.correct/self.data_size * 100)
        result = f" Your Score is : {score}%"
        mb.showinfo("Result Status",f"{result}\n{correct}\n{wrong}")
    def buttons(self):
        next_button = Button(root,text="Next", bg="green",command=self.next_btn,fg="white", font=("ariel",16,"bold"))
        next_button.place(x=300,y=350)
        quit_button = Button(root,text="Quit", bg="green",fg="white",command=root.destroy, font=("ariel",16,"bold"))
        quit_button.place(x=700,y=50)
root=Tk()
root.geometry("800x450")
root.title("NIIT EXAMINATION APP")
with open('data.json') as f:
    data = json.load(f)
question = (data['question'])
options = (data['options'])
answer = (data['answer'])
quiz = Quiz()
root.mainloop()