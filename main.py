# Company Tracker project.

# Name
# Job Title
# Location
# Website
# Last Applied Date
# General Application
# Applied For
# Cover Letter
# Note

import tkinter as tk
from tkinter import ttk

category = (
        "Company Name",
        "Job Title",
        "Location",
        "Website",
        "Last Date Applied",
        "General Application",
        "Cover Letter",
        "Note",
        )
        
root = tk.Tk()
root.minsize(500,350)

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

sheetFrame = ttk.Frame(root)
buttonFrame = ttk.Frame(root)


def createAddWindow():
    window = tk.Toplevel(root)
    window.title("Add")
    cateSize = len(category)
    entries = []
    
    # Place UI on window
    for i in range(cateSize):
        label = ttk.Label(window, text=category[i])
        entry = ttk.Entry(window)
        entries.append(entry)
        label.grid(row=i, column=0)
        entry.grid(row=i, column=1)
    
    # Button functionality
    cancelBtn = ttk.Button(window, text="Cancel", command=lambda: window.destroy())
    cancelBtn.grid(row=cateSize, column=0)
    
    acceptBtn = ttk.Button(window, text="Add", command=lambda: addNewEntry(entries, window))
    acceptBtn.grid(row=cateSize, column=1)
    
    
def addNewEntry(entries, window):
    inp = []
    for entry in entries:
        inp.append(entry.get())
    treeview.insert(
                "",
                tk.END, 
                values=inp
                )
    window.destroy()

def deleteRow():
    iid = treeview.focus()
    treeview.delete(iid)

# Buttons
addBtn = ttk.Button(buttonFrame, command=createAddWindow, text="Add")
addBtn.pack(side=tk.LEFT, padx=10)
deleteBtn = ttk.Button(buttonFrame, command=deleteRow, text="Delete")
deleteBtn.pack(side=tk.LEFT, padx=10)
ttk.Frame(buttonFrame, width=10).pack(side=tk.LEFT)
findEntry = ttk.Entry(buttonFrame)
findEntry.pack(side=tk.LEFT)
findBtn = ttk.Button(buttonFrame, text="Find")
findBtn.pack(side=tk.LEFT)

treeview = ttk.Treeview(
    sheetFrame,
    columns=category,
    show="headings",
)

for i in category:
    treeview.heading(i, text=i)
    treeview.column(i, width=150)
    
def getTreeview():
    return treeview

# treeview.heading("Name", text="Company Name")
# treeview.heading("Title", text="Job Title")
# treeview.heading("Location", text="Location")
# treeview.heading("Website", text="Website")
# treeview.heading("Date", text="Last Date Applied")
# treeview.heading("General Application", text="General Application")
# treeview.heading("Cover Letter", text="Cover Letter")
# treeview.heading("Note", text="Notes")

# treeview.column("Name", width=150)
# treeview.column("Title", width=150)
# treeview.column("Location", width=150)
# treeview.column("Website", width=150)
# treeview.column("Date", width=150)
# treeview.column("General Application", width=150)
# treeview.column("Cover Letter", width=150)
# treeview.column("Note", width=150)

treeview.insert(
                "",
                tk.END, 
                values=(
                    "XYZ",
                    "Intern",
                    "Vancouver",
                    "www.google.ca",
                    "2026-02-09",
                    "Yes",
                    "No",
                    "N/A"
                    )
                )

# Scrollbars
v_scrollbar = ttk.Scrollbar(sheetFrame, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=v_scrollbar.set)
h_scrollbar = ttk.Scrollbar(sheetFrame, orient=tk.HORIZONTAL, command=treeview.xview)
treeview.configure(xscrollcommand=h_scrollbar.set)



def delEntry(event):
    event.widget.destroy()
   
def acceptEntry(event, row, col):
    info = event.widget.get()
    treeview.set(row, column=col, value=info)
    event.widget.destroy()

def createEntryEdit(row, col):
    x, y, width, height = treeview.bbox(row, col)
    entry = ttk.Entry(sheetFrame)
    entry.bind("<FocusOut>", delEntry)
    entry.bind("<Return>", lambda event: acceptEntry(event, row, col))
    entry.focus_set()
    entry.place(x=x, y=y)
    
def editEntry(event):
    row = treeview.identify_row(event.y)
    col = int(treeview.identify_column(event.x)[1:])
    
    print(treeview.item(row, 'values'))
    
    createEntryEdit(row, col-1)
    
treeview.bind("<Double-1>", editEntry)


    
# Resize
def resize_window(event):
    if(event.widget == root):
        winWeight = root.winfo_width()
        winHeight = root.winfo_height()
        root.columnconfigure(0, weight=winWeight)  
        root.rowconfigure(1, weight=winHeight)
root.bind("<Configure>", resize_window)

h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True);
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


buttonFrame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
sheetFrame.grid(row=1, column=0, sticky="nsew")

root.mainloop()