# Company Tracker project.
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

def main():
    app = App()
    
class App:
    def __init__(self):
        self.category = (
                        "Company Name",
                        "Job Title",
                        "Location",
                        "Website",
                        "Last Date Applied",
                        "General Application",
                        "Cover Letter",
                        "Note"
                        )
        # App's main window
        self.root = tk.Tk()
        self.root.minsize(500,350)
        
        # Sections of the main window.
        self.sheetFrame = ttk.Frame(self.root)
        self.treeview = ttk.Treeview(
            self.sheetFrame,
            columns=self.category,
            show="headings",
        )           
        self.buttonFrame = ttk.Frame(self.root)    
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu) 
            
        # Call functions to create each part of the main window.
        self.createDataview()
        self.createButtons()
        self.createMenu()

        self.root.bind("<Configure>", self.resize_window)
        self.root.mainloop()                    
     
    ## Create topbar menu
    def createMenu(self):
        def openFile():
            filePath = filedialog.askopenfilename()
            df = pd.read_csv(filePath)
            
            for row in self.treeview.get_children():
                self.treeview.delete(row)
            for row in df.values:
                self.treeview.insert('', 'end', values=tuple(row))
            
        def saveFile():
            filePath = filedialog.asksaveasfilename()
            
            # Get data
            children = self.treeview.get_children()
            data = []
            for child in children:  
                row = self.treeview.item(child)['values']
                data.append(row)
                
            #Save data
            df = pd.DataFrame(data, columns=self.category)
            df.to_csv(filePath, index=False)
            
        # File Menu    
        fileMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open", command=openFile)
        fileMenu.add_command(label="Save", command=saveFile)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.root.quit)

    ## Create the the sheetframe that will display the data and returns the treeview that interacted with outside.
    def createDataview(self):
        for i in self.category:
            self.treeview.heading(i, text=i)
            self.treeview.column(i, width=150)
            
        def delEntry(event):
            event.widget.destroy()
           
        def acceptEntry(event, row, col):
            info = event.widget.get()
            self.treeview.set(row, column=col, value=info)
            event.widget.destroy()
            
        def createEntryEdit(row, col):
            x, y, width, height = self.treeview.bbox(row, col)
            entry = ttk.Entry(self.sheetFrame)
            entry.bind("<FocusOut>", delEntry)
            entry.bind("<Return>", lambda event: acceptEntry(event, row, col))
            entry.focus_set()
            entry.place(x=x, y=y)
            
        def editEntry(event):
            row = self.treeview.identify_row(event.y)
            col = int(self.treeview.identify_column(event.x)[1:])

            createEntryEdit(row, col-1)
            
        def columnSort(col):
            items = []
            for i in self.treeview.get_children():
                items.append(i)
            
            index = self.category.index(col)
            items.sort(key=lambda item: self.treeview.item(item)['values'][index])
            
            for i, row in enumerate(items):
                self.treeview.move(row, '', i)
        
        # Functionality for treeview (entries)
        self.treeview.bind("<Double-1>", editEntry)
        for col in self.category:
            self.treeview.heading(col, command=lambda x=col: columnSort(x))

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(self.sheetFrame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=v_scrollbar.set)
        h_scrollbar = ttk.Scrollbar(self.sheetFrame, orient=tk.HORIZONTAL, command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=h_scrollbar.set)
        
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True);
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.sheetFrame.grid(row=1, column=0, sticky="nsew")

    # Create the buttons on the main window
    def createButtons(self):
        ## Functions of the all the buttons (Add, Delete, Find)
        # Add button functionality
        def createAddWindow():
            window = tk.Toplevel(self.root)
            window.title("Add")
            cateSize = len(self.category)
            entries = []
            
            # Place UI on window
            for i in range(cateSize):
                label = ttk.Label(window, text=self.category[i])
                entry = ttk.Entry(window)
                entries.append(entry)
                label.grid(row=i, column=0, padx=10, pady=10)
                entry.grid(row=i, column=1, padx=10, pady=10)
            
            # Button functionality
            cancelBtn = ttk.Button(window, text="Cancel", command=lambda: window.destroy())
            cancelBtn.grid(row=cateSize, column=0, padx=10, pady=10)
            
            acceptBtn = ttk.Button(window, text="Add", command=lambda: addNewEntry(entries, window))
            acceptBtn.grid(row=cateSize, column=1, padx=10, pady=10)
              
        def addNewEntry(entries, window):
            inp = []
            for entry in entries:
                inp.append(entry.get())
            self.treeview.insert(
                        "",
                        tk.END, 
                        values=inp
                        )
            window.destroy()
        
        # Delete button functionality
        def deleteRow():
            iid = self.treeview.focus()
            self.treeview.delete(iid)
            
        # Find button functionality
        detachedItems = []
        def find(x):
            # reattach previously detached items
            for idd, i in detachedItems:
                self.treeview.move(idd, "", i)
            detachedItems.clear()
            
            # find all items to detach (remove)
            entry = x.get().lower()
            if(entry == ""):
                return
            for i, idd in enumerate(self.treeview.get_children()):
                lst = ' '.join(self.treeview.item(idd)['values']).lower()
                if entry not in ''.join(lst):
                    detachedItems.insert(0, (idd, i))
                    self.treeview.detach(idd)
                    
        
        # Add UI for the buttons
        addBtn = ttk.Button(self.buttonFrame, command=createAddWindow, text="Add")
        addBtn.pack(side=tk.LEFT, padx=10)
        
        deleteBtn = ttk.Button(self.buttonFrame, command=deleteRow, text="Delete")
        deleteBtn.pack(side=tk.LEFT, padx=10)
        
        ttk.Frame(self.buttonFrame, width=10).pack(side=tk.LEFT) # empty spacer
        findEntry = ttk.Entry(self.buttonFrame)
        findEntry.pack(side=tk.LEFT)
        
        findBtn = ttk.Button(self.buttonFrame, command=lambda: find(findEntry), text="Find")
        findBtn.pack(side=tk.LEFT)
        
        self.buttonFrame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
    def resize_window(self, event):
        if(event.widget == self.root):
            winWeight = self.root.winfo_width()
            winHeight = self.root.winfo_height()
            self.root.columnconfigure(0, weight=winWeight)  
            self.root.rowconfigure(1, weight=winHeight)


if __name__ == "__main__":
    main()
