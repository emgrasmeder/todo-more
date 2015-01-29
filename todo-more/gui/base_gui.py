#base_gui.py
from tkinter import *
import time

class App:
    def __init__(self):
        self.master = Tk()
        self.master.title("todo more")
        self.row_count = 0
        self.cols = {"submit":[0,"Submit Entry",self.submit_entry],
                    "text_field":[1,"",None],
                    "add_new": [2, "Add Another Item",
                                        self.add_fields]}
        
        self.add_button(btype="add_new")

        self.master.mainloop()

    def add_fields(self, ttype="text_field"):
        if ttype:
            self.field_input=Entry(self.master)
            self.field_input.grid(row=self.row_count,
                                column=self.cols[ttype][0])
            self.row_count += 1 #this can be unit tested 

    def add_button(self,btype=None):
        if btype:
            self.new_field_button = Button(self.master,
                                            text=self.cols[btype][1],
                                            command=self.cols[btype][2])
            self.new_field_button.grid(row=self.row_count,column=\
                                                self.cols[btype][0])


    def submit_entry(self, entry=None):
        if entry:
            print("Your input, '%s,' was [not] saved to your todo file" %
                entry)

App()