import datetime
import os

class TodoFile():
    '''
        Opens, reads in, appends to, and generally manages
        communication between todo-more logic and the todo file.

        An instance of TodoFile is created when user runs the 
        Python file. 
    '''
    def __init__(self, debug=False, todo_file="default",has_headers=True):
        if todo_file == "default":
            filename = "sorted_ideas.csv"
            path = "/home/emma/Dropbox/"
            self.debug=debug
            self.cleaned_file = False
            self.has_headers = has_headers
            self.headers = ["ID",
                            "Importance",
                            "StartDate",
                            "Category",
                            "Description",
                            "ExtraInformation",
                            "Solution",
                            "CompletionDate"]

            self.fullpath = os.path.join(path, filename)
            with open(self.fullpath) as f:
                self.todo_file = [line.split('\t') for line in f]
            
            self.start_date_index= self.get_header_index("StartDate")
            self.index_index = self.get_header_index("ID")
        else:
            raise Exception("TodoFile can't handle any arguments yet.")

    def get_header_index(self,header):
        if header:
            index = [index 
                        for index,item in enumerate(self.headers) 
                            if header == item]
            return(index[0])
        else:
            input("Argument Error: get_header_index can't handle headerless\
                data sets yet")
     
    def clean_file(self):
        '''
            Cleaned File is the input file without headers, training newlines
            or blank entries (based on input date, which should always exist)
        '''
        if self.has_headers:
            loc_cleaned_file = list(filter(lambda record: 
                        record[self.get_header_index("StartDate")]!="",
                            self.todo_file[1:]))
            return(loc_cleaned_file)
        else:
            input("Can't Handle headerless data sets yet")
            exit()
            return(list(filter(lambda record: 
                        record[self.get_header_index("StartDate")]!="",
                            self.todo_file)))
    
    def get_input(self):
            print('''
            The [eventual] format for adding an item:
                Importance: integer
                StartDate: [yyyy-mm-dd]
                Category: string
                Description: string
                Extra information: string
                Solution: string (hardcoded x)
                Completion Date
                ******
                Shortcuts: -r, -d, -c, -d, -e, -s
                Default input order: Description, Category, Importance
                Override defaults with shortcuts.''')
            category = input("Category: ")
            description = input("Description: ")
            importance = input("Importance: ")
            extra_info = input("Extra info: ")

            return(description, category, importance, extra_info)


    def new_entry(self):
        '''
            Creates a new row entry based on user input.
        '''
        description, category, importance, extra_info = self.get_input()
        self.insert_input(new_entry=True,
                            description=description,
                            category=category,
                            importance=importance,
                            extra_info=extra_info)

    def insert_input(self, **kwargs):
        f_new = open(self.fullpath, 'w')
        f_new.write("\t".join(self.headers)+"\n")
        for line in self.cleaned_file:
            if "\n" not in line[-1]:
                line[-1]+="\n"
            f_new.write("\t".join(line))
        if kwargs:
            f_new.write("\t".join(
                [str(self.get_record(record_id="max")+1),
                kwargs["importance"],
                self.current_date(),
                kwargs["category"],
                kwargs["description"],
                kwargs["extra_info"],
                "x",
                "x"
                ]))


    def current_date(self):
        return datetime.datetime.now().isoformat()[:10]

    def get_record(self, record_id=False):
        if not self.cleaned_file:
            self.cleaned_file = self.clean_file()
            #print(self.cleaned_file)
        if record_id != "max":
            for record in self.cleaned_file:
                if int(record[self.get_header_index("ID")])==int(record_id):    
                    return(record)                 
            
            #return(therecord) #a list --maybe in a list? :(
        else: #if record_id = "max"
            ''' Returns int(max_record_id)'''
            max_record_id = list(map(lambda record: 
                int(record[self.get_header_index("ID")]),
                    self.cleaned_file))
            #print("max_rec_id: ",max(max_record_id))
            return(int(max(max_record_id)))

    def close_item(self, purpose="close",record_id=False):
        '''
            
        '''
        def update_that_line(index):
            self.cleaned_file[index][self.get_header_index("CompletionDate")] = \
                                                        self.current_date()
            return(self.cleaned_file[index])
        if not self.cleaned_file:
            self.cleaned_file = self.clean_file()
        for index, row in enumerate(self.cleaned_file):
            if record_id == row[self.get_header_index("ID")]:
                verify = input("Are you sure you'd like to mark %s as \
                    completed on todays date? [y\\n] \n Response: " % self.cleaned_file[index])
                if verify.lower().strip() in ["y","yes"]:
                    update_that_line(index)
                    print("\n.\n.\n.\nItem Closed")
        self.insert_input() 



    def sort():
        '''
            Re-arrange items according to listed categories
        '''
        pass