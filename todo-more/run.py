#run.py
import TodoFile
f = TodoFile.TodoFile()
mode = input("Enter Mode: ")
if mode =="":
    print(f.get_record(record_id="max") )
elif "c" in mode:
    record_id = mode.split(' ')[1]
    print(record_id)
    f.close_item(record_id=record_id)
elif mode == "run":
    f.new_entry()