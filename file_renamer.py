import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer")
        self.root.geometry("600x600")
        self.files = []
        
        # Styling
        self.label_font = ("Helvetica", 12)
        self.entry_font = ("Helvetica", 10)
        self.button_font = ("Helvetica", 10)
        
        # UI Elements
        self.label = tk.Label(root, text="Select files to rename:", font=self.label_font)
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Files", font=self.button_font, command=self.select_files)
        self.select_button.pack(pady=5)

        self.renamed_files_listbox = tk.Listbox(root, width=80, height=10, font=self.entry_font)
        self.renamed_files_listbox.pack(pady=5)

        self.prefix_label = tk.Label(root, text="Prefix:", font=self.label_font)
        self.prefix_label.pack(pady=5)
        self.prefix_entry = tk.Entry(root, font=self.entry_font)
        self.prefix_entry.pack(pady=5)

        self.suffix_label = tk.Label(root, text="Suffix:", font=self.label_font)
        self.suffix_label.pack(pady=5)
        self.suffix_entry = tk.Entry(root, font=self.entry_font)
        self.suffix_entry.pack(pady=5)

        self.middle_label = tk.Label(root, text="Replace middle with:", font=self.label_font)
        self.middle_label.pack(pady=5)
        self.middle_entry = tk.Entry(root, font=self.entry_font)
        self.middle_entry.pack(pady=5)

        self.keep_original_var = tk.IntVar()
        self.keep_original_check = tk.Checkbutton(root, text="Keep original file name", font=self.label_font, variable=self.keep_original_var)
        self.keep_original_check.pack(pady=5)

        self.rename_button = tk.Button(root, text="Rename Files", font=self.button_font, command=self.rename_files)
        self.rename_button.pack(pady=10)

        self.status_label = tk.Label(root, text="", font=self.label_font)
        self.status_label.pack(pady=10)

    def select_files(self):
        self.files = filedialog.askopenfilenames()
        self.update_listbox()

    def rename_files(self):
        prefix = self.prefix_entry.get().strip()
        suffix = self.suffix_entry.get().strip()
        middle = self.middle_entry.get().strip()
        keep_original = self.keep_original_var.get()

        if keep_original and middle:
            messagebox.showerror("Error", "Cannot rename files with a middle part if 'Keep original file name' is checked.")
            return

        prefix = f"{prefix}_" if prefix else ""
        suffix = f"_{suffix}" if suffix else ""

        new_files = []

        for i, file_path in enumerate(self.files):
            directory, filename = os.path.split(file_path)
            name, ext = os.path.splitext(filename)

            name = name.replace(" ", "_")

            if not keep_original:
                name = middle if middle else ""
            else:
                name = f"{name}_{middle}" if middle else name

            new_name = f"{prefix}{name}{suffix}_{i+1}{ext}".replace("__", "_")
            new_path = os.path.join(directory, new_name)
            os.rename(file_path, new_path)
            new_files.append(new_path)

        self.files = new_files
        self.update_listbox()
        self.status_label.config(text="Files have been renamed")
        self.clear_entries()

    def update_listbox(self):
        self.renamed_files_listbox.delete(0, tk.END)
        for file_path in self.files:
            self.renamed_files_listbox.insert(tk.END, file_path)

    def clear_entries(self):
        self.prefix_entry.delete(0, tk.END)
        self.suffix_entry.delete(0, tk.END)
        self.middle_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamer(root)
    root.mainloop()
