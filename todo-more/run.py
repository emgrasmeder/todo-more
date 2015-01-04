#run.py
import TodoFile
f = TodoFile.TodoFile()
if input("Enter Mode: ") != "run":
    f.get_record(record_id="max")
else:
    f.new_entry()