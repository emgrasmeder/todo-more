import datetime
import os

class TodoFile():
    '''
        Opens, reads in, appends to, and generally manages
        communication between todo-more logic and the todo-file.

        An instance of TodoFile is created when user runs the 
        Python file. 
    '''
    def __init__(self, debug=False, todo_file="default"):
        if todo_file == "default":
            filename = "sorted_ideas.csv"
            path = "/home/emma/Dropbox/"
            self.debug=debug
            self.fullpath = os.path.join(path, filename)
            self.split_file()
        else:
            raise Exception("TodoFile can't handle any arguments yet.")

    def split_file(self):
        with open(self.fullpath) as f:
            the_split_file = [line.split('\t') for line in f]
            if self.debug:
                print(the_split_file)
            return the_split_file

    def find_line(self, specific=False, **kwargs):
        '''
            I'm not sure if this is the optimal way to write the algorithm,
            but this method will by default find the next line, otherwise 
            find the line you ask it to, by the index. 
        '''
        if specific:
            pass
        else:   #Find the next empty line
            for line in self.split_file():
                if line[0]:
                    max_index = line[0]
                    print(max_index)
        return max_index


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
