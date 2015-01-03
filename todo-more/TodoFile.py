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
                if self.debug:
                    return(self.todo_file)
            self.start_date_index= self.get_header_index("StartDate")
            self.index_index = self.get_header_index("ID")
        else:
            raise Exception("TodoFile can't handle any arguments yet.")

    def get_header_index(self,header):

        index = [index 
                    for index,item in enumerate(self.headers) 
                        if header == item]
        print("index: ",index[0])
        return(index[0])


    def get_next_empty_row(self,
                    specific_row=False,
                    headers=True,
                    **kwargs):
        '''
            I'm not sure if this is the optimal way to write the algorithm,
            but this method will by default find the next line, otherwise 
            find the line you ask it to, by the index. 
        '''
        if specific_row:
            pass
        else:
            if headers:
                cleaned_file =\
                    (list(filter(lambda line: 
                        line[self.start_date_index]!="",self.todo_file)))
                return(int(max(
                    list(
                        map(lambda row: row[0], cleaned_file[1:])
                            )))+1)
            else:
                #self.prepend_headers()
                pass

    def new_entry(self):
        empty_row_index = self.get_next_empty_row()
        def get_input():
            import add_item
            new_entry = add_item.new_entry()
            print(new_entry)

        def parse_input():
            pass
        def insert_input():
            pass

        get_input()
        parse_input()
        insert_input()


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
