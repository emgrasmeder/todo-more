import datetime
import os

class TodoFile():
    '''
        Opens, reads in, appends to, and generally manages
        communication between todo-more logic and the todo-file.

        An instance of TodoFile is created when user runs the 
        Python file. 
    '''
    def __init__(self, todo_file="default"):
        if todo_file == "default":
            filename = "sorted_ideas.csv"
            path = "/home/emma/Dropbox/"
            fullpath = os.path.join(path, filename)

            with open(fullpath) as f:
                print([line.split('\t') for line in f])
        else:
            raise Exception("TodoFile can't handle any arguments yet.")

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
