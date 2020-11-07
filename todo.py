from tkinter import *

# #Variables
color_primary = "#16211a"
color_secondary = "#6bbf8d"
color_white = "#fff"
color_grey = "#7c7d7d"

#window setup

root = Tk()
root.title('Tykel todo')
root.configure(background=color_primary)




done = StringVar()

t = "Finish this app"
taskFrame = LabelFrame(root,pady=10,padx=10,bd=0)
taskFrame.configure(background=color_primary)
# add and search functionalities
def add_todo(task):

    todo = Checkbutton(taskFrame,bg=color_primary,fg=color_white,text=f'{task}',variable=done,onvalue="done",offvalue="undone",anchor=W,command = lambda:strikethrough(t,done.get()))
    todo.deselect()
    todo.pack(fill=(X))
    addTodo.delete(0,END)


todo = Checkbutton(taskFrame,bg=color_primary,bd=0,fg=color_white,text=f'{t}',variable=done,onvalue="done",offvalue="undone",anchor=W,command = lambda:strikethrough(t,done.get()))
todo.deselect()

search = Entry(root,width=30,bg=color_secondary)
btn_search = Button(root,text="Search")
addTodo= Entry(root,width=30,bg=color_secondary)
btn_add= Button(root,text="Add Todo",command= lambda:add_todo(addTodo.get()))

# #functions
def strikethrough(word,progress):
    """
        this cancel the done task
    """
    global todo
    
    print(progress)
    if progress == "done":
        todo.forget()
        todo = Checkbutton(taskFrame,bg=color_primary,bd=0,fg=color_grey,text=f'{word}',font=("Helvetica","90",'overstrike'),variable=done,onvalue="done",offvalue="undone",anchor=W,command = lambda:strikethrough(t,done.get()))
    elif progress == 'undone':

        todo.forget()
        todo = Checkbutton(taskFrame,bg=color_primary,bd=0,fg=color_white,text=f'{word}',font=("Helvetica",30),variable=done,onvalue="done",offvalue="undone",anchor=W,command = lambda:strikethrough(t,done.get()))

    todo.pack(fill=(X))
    #     print('done')



# #Layout and display setup
search.grid(row=0,column=0,pady=10)
btn_search.grid(row=0,column=1,pady=10)

taskFrame.grid(row=1,column=0,columnspan=2)
todo.pack(side='left',fill=(X))
addTodo.grid(row=2,column=0,pady=10)
btn_add.grid(row=2,column=1,pady=10,padx=5)

mainloop()