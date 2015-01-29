#base_gui.py
from tkinter import *
import time

class App:
    '''
        Inspired by Ryan Godfrey's YouTube tutorial about tkinter 
        (https://www.youtube.com/watch?v=v8YQYKDqLME), the App instance
        creates a pop up GUI, which will eventually be how the user interacts
        with todo-more. 

        Right now the GUI has a button that adds new text fields, which 
        actually send input back to the class object, but the retrieve button
        hasn't been added yet. 

        Some tasks for the future:
            - **If you kill the program without exiting out of the GUI, 
                the GUI stays alive forever.**
            - GUI input communicates with already functional (cli) code.
            - Add "new text field" in the same record for multiple entries in 
                the same row
            - Default text in the input text fields (that goes away on
                mouseclick) (see: https://mail.python.org/pipermail/tutor/2011-August/085092.html)
            - Hide/Remove Input rows from GUI
            - GUI to display data from todo textfile

    '''
    def __init__(self):
        '''
            Creates GUI with one button to get started.
        '''
        self.outputs = False
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
        '''
            Adds next text field, ready for input.
        '''

        if ttype:
            self.usertext = StringVar()
            #self.usertext.set("Enter some input")
            self.field_input = Entry(self.master,
                                    textvariable=self.usertext)
            self.field_input.grid(row=self.row_count,
                                column=self.cols[ttype][0])
            self.add_button(btype="submit") #what if it's already there?

            self.row_count += 1 #this can be unit tested

    def add_button(self,btype=None):
        '''
            To add either "Add New Row" type button, or "Add Another Text 
            Field" type button. Can be used to add any sort of button to 
            GUI, including "edit","undo","delete", and so on.
        '''
        if btype:
            self.new_field_button = Button(self.master,
                                            text=self.cols[btype][1],
                                            command=self.cols[btype][2])
            self.new_field_button.grid(row=self.row_count,column=\
                                                self.cols[btype][0])


    def submit_entry(self, entry=None):
        '''
            To show the developer print-function feedback about what is
            being ouput from text fields, and to send data to "to do.txt"

            Known Issues:
                - self.usertext.get() only looks at the most recently created
                    text field. Each usertext instance needs to be unique,
                    stored either in a dict or a list.
        '''

        print("Your input was, '%s,' and someday we'll save it to a file." %
                self.usertext.get())

App()