import tkinter as tk
from tkinter import filedialog
import pandas as pd

class CSVProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV File Processor")
        
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack()

        self.file_label = tk.Label(self.main_frame, text="Drag and drop CSV file here:")
        self.file_label.grid(row=0, column=0, pady=10)

        self.file_drop_area = tk.Label(self.main_frame, bg="lightgray", width=50, height=5, text="Drop File Here", padx=10, pady=10)
        self.file_drop_area.grid(row=1, column=0)

        self.file_drop_area.bind("<Button-1>", self.browse_file)
        self.file_drop_area.bind("<B1-Motion>", self.drag_over)
        self.file_drop_area.bind("<ButtonRelease-1>", self.drop_file)

    def browse_file(self, event=None):
        filename = filedialog.askopenfilename()
        if filename:
            self.process_csv(filename)

    def drag_over(self, event=None):
        self.file_drop_area.configure(bg="lightblue")
    
    def drop_file(self, event=None):
        self.file_drop_area.configure(bg="lightgray")
        if event.data:
            filename = self.root.tk.splitlist(event.data)[0]
            self.process_csv(filename)

    def process_csv(self, filename):
        # Read the CSV file and include only the specified columns
        df = pd.read_csv(filename, usecols=["From: (Address)"])
        df2 = pd.read_csv(filename, usecols=["CC: (Address)"])

        # Remove duplicate rows
        df = df.drop_duplicates()
        df2 = df2.drop_duplicates()

        # Write the DataFrame to new CSV files
        df.to_csv('toEmails.csv', index=False)
        df2.to_csv('ccEmails.csv', index=False)

        tk.messagebox.showinfo("CSV Processing", "CSV files processed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVProcessorApp(root)
    root.mainloop()
