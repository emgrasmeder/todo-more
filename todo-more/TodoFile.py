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
            self.fullpath = os.path.join(path, filename)
            with open(self.fullpath) as f:
                self.todo_file = [line.split('\t') for line in f]
                if self.debug:
                    return(self.todo_file)
            self.date_index, self.index_index = self.get_base_indices()
        else:
            raise Exception("TodoFile can't handle any arguments yet.")

    def get_base_indices(self):

        return self.todo_file[0].index("Date Added"),\
                                    self.todo_file[0].index("ID")


    def find_line(self, specific=False,headers=True, **kwargs):
        '''
            I'm not sure if this is the optimal way to write the algorithm,
            but this method will by default find the next line, otherwise 
            find the line you ask it to, by the index. 
        '''
        if specific:
            pass
        else:
            if headers:
                cleaned_file =\
                    (list(filter(lambda line: 
                        line[self.date_index]!="",self.todo_file)))
                return(max(
                    list(
                        map(lambda row: row[0], cleaned_file[1:])
                            )))



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
