#run.py
import todofile
f = todofile.TodoFile()
mode = input("Enter Mode: (\"run\",\n OR\n\"close item N\"): ")

if "close item" in mode:
    record_id = mode.split(' ')[1]
    print(record_id)
    f.close_item(record_id=record_id)
elif mode == "run":
    f.new_entry()