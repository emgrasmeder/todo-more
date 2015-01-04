import TodoFile

def new_entry():
    return(input("The format for adding an item:\
    Importance: integer\
    StartDate: [yyyy-mm-dd]\
    Category: string\
    Description: string\
    Extra information: string\
    Solution: string (hardcoded x)\
    Completion Date\
    ******\
    Shortcuts: -r, -d, -c, -d, -e, -s\
    Default input order: Description, Category, Importance\
    Override defaults with shortcuts.\
    Enter task:"))