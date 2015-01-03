import TodoFile

new_input = input("The format for adding an item:\
    Rating: integer\
    Date added: [yyyy-mm-dd]\
    Category: string\
    Description: string\
    Extra information: string\
    Solution: string (hardcoded x)\
    ******\
    Shortcuts: -r, -d, -c, -d, -e, -s\
    Default input order: Category, Description, Importance\
    Override defaults with shortcuts.\
    Enter task:")

#print(new_input)
a_file = TodoFile.TodoFile()#debug=True)
print(a_file.find_line())