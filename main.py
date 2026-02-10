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

root = tk.Tk()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

sheetFrame = ttk.Frame(root);
buttonFrame = ttk.Frame(root);

# Buttons
addBtn = ttk.Button(buttonFrame, text="Add")
addBtn.pack(side=tk.LEFT, padx=10)
deleteBtn = ttk.Button(buttonFrame, text="Delete")
deleteBtn.pack(side=tk.LEFT, padx=10)
ttk.Frame(buttonFrame, width=10).pack(side=tk.LEFT)
findEntry = ttk.Entry(buttonFrame)
findEntry.pack(side=tk.LEFT)
findBtn = ttk.Button(buttonFrame, text="Find")
findBtn.pack(side=tk.LEFT)

treeview = ttk.Treeview(
    sheetFrame,
    columns=(
        "Name",
        "Title",
        "Location",
        "Website",
        "Date",
        "General Application",
        "Cover Letter",
        "Note",
    ),
    show="headings",
)

treeview.heading("Name", text="Company Name")
treeview.heading("Title", text="Job Title")
treeview.heading("Location", text="Location")
treeview.heading("Website", text="Website")
treeview.heading("Date", text="Last Date Applied")
treeview.heading("General Application", text="General Application")
treeview.heading("Cover Letter", text="Cover Letter")
treeview.heading("Note", text="Notes")

treeview.column("Name", width=150)
treeview.column("Title", width=150)
treeview.column("Location", width=150)
treeview.column("Website", width=150)
treeview.column("Date", width=150)
treeview.column("General Application", width=150)
treeview.column("Cover Letter", width=150)
treeview.column("Note", width=150)

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

h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True);
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


buttonFrame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
sheetFrame.grid(row=1, column=0, sticky="nsew")

root.mainloop()