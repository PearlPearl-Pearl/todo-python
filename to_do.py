import tkinter as tk
import sqlite3 as sql


tasks=[]
def add_task():
        # the user will type in the task in the entry field. You then get the string and add that to the tasks list.
        task_string=enter_field.get()
        tasks.append(task_string)
        text_listbox.insert('end',task_string)
        cursor.execute('insert into task(task_text) values(?)', (task_string,))
        enter_field.delete(0, 'end')


def delete_task():
    the_value=text_listbox.get(text_listbox.curselection())
    tasks.remove(the_value)
    text_listbox.delete(0, 'end')
    for task in tasks:
        text_listbox.insert('end', task)
    cursor.execute('delete from task where task_text=?', (the_value,))


def delete_all_tasks():
    while len(tasks)>0:
        tasks.pop()
    text_listbox.delete(0,'end')
    cursor.execute('delete from task')


def exit_app():
    print(f'These are your tasks for today {tasks}')
    guiWindow.destroy()



if __name__=='__main__':
    guiWindow = tk.Tk(className='Hello World To-Do App')

    todo_label=tk.Label(master=guiWindow, text='To-Do List')
    todo_label.grid(row=0, columnspan=2)

    enter_label=tk.Label(master=guiWindow, text='Enter the task:')
    enter_label.grid(row=2, column=0)

    enter_field=tk.Entry(master=guiWindow, width=26)
    enter_field.grid(row=3, column=0)

    add_button=tk.Button(master=guiWindow, text='Add Task', command=add_task, width=24)
    add_button.grid(row=4, column=0)

    delete_button=tk.Button(master=guiWindow, text='Delete Task', width=24, command=delete_task)
    delete_button.grid(row=5, column=0)

    delete_all_button=tk.Button(master=guiWindow, text='Delete All Tasks', width=24, command=delete_all_tasks)
    delete_all_button.grid(row=6, column=0)

    exit_button=tk.Button(master=guiWindow, text='Exit', width=24, command=exit_app)
    exit_button.grid(row=7, column=0)

    text_listbox=tk.Listbox(master=guiWindow,
    width = 26,  
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF")
    text_listbox.grid(row=1, column=1, rowspan=6, padx=10, pady=(10, 0))

    connection=sql.connect('taskList.db')
    cursor=connection.cursor()

    cursor.execute('create table if not exists task(task_text varchar(255))')

    guiWindow.mainloop()

    

# if __name__=='__main__':
#     main()