import datetime
import os

class TodoFile():
    '''
        Opens, reads in, appends to, and generally manages
        communication between todo-more logic and the todo file.

        An instance of TodoFile is created when user runs the 
        Python file. 
    '''
    def __init__(self, debug=False, todo_file="default"):
        if todo_file == "default":
            filename = "sorted_ideas.csv"
            path = "/home/emma/Dropbox/"
            self.debug=debug
            self.cleaned_file = False
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
            
            self.start_date_index= self.get_header_index(header="StartDate")
            self.index_index = self.get_header_index(header="ID")
        else:
            raise Exception("TodoFile can't handle any arguments yet.")

    def get_header_index(self,header=False):
        if header:
            index = [index 
                        for index,item in enumerate(self.headers) 
                            if header == item]
            return(index[0])
        else:
            raise InputError("get_header_index requires a header to find")

    def get_record(self, record_id=False):
        if record_id != "max":
            record = list(filter(
                        lambda record: 
                            int(record[self.get_header_index(header="ID")]
                                )==record_id, self.cleaned_file))
            print(record)
        else: #if record_id = "max"
            if not self.cleaned_file:
                self.cleaned_file = self.clean_file()
                max_record_id = list(map(lambda record: 
                    int(record[self.get_header_index(header="ID")]),
                        self.cleaned_file))
                return(int(max(max_record_id)))
     
    def clean_file(self, headers=True):
        '''
            Cleaned File is the input file without headers, training newlines
            or blank entries (based on input date, which should always exist)
        '''
        if headers:
            return(list(filter(lambda record: 
                        record[self.get_header_index(header="StartDate")]!="",
                            self.todo_file[1:])))
        else:
            return(list(filter(lambda record: 
                        record[self.get_header_index(header="StartDate")]!="",
                            self.todo_file)))
    def new_entry(self):
        empty_row_index = self.get_record(record_id="max")+1
        print("empty row index = ",empty_row_index)
        input()
        def get_input():
            print('''
            The format for adding an item:
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

            description = input('Task Description: ')
            category = input('Category: ')
            importance = input('Importance: ')
            extra_info = input('Extra Information: ')
            return(description, category, importance, extra_info)
        def insert_input(description, category, importance, extra_info):
            f_new = open(self.fullpath, 'w')
            for line in self.cleaned_file:
                f_new.write("\t".join(line))
            f_new.write("\t".join(["\n"+str(empty_row_index),
                                    importance,
                                    datetime.datetime.now().isoformat()[:10],
                                    category,
                                    description,
                                    extra_info,
                                    "x",
                                    "x"]))

            

        description, category, importance, extra_info = get_input()
        insert_input(description, category, importance, extra_info)


    def sort():
        '''
            Re-arrange items according to listed categories
        '''
        pass
    def query():
        '''
            Returns record based on search term
        '''
        pass
    def delete():
        '''
            Permanently deletes item, requires input: 
                "delete item [index_number]" 
        '''
        pass