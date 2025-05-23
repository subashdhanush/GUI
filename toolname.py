import tkinter as tk

def show_name():
    name = name_entry.get()
    output_label.config(text=f"Hello, {name}!")

# Create the main window
root = tk.Tk()
root.title("Hello Tkinter")

# Label
tk.Label(root, text="Enter your name:").pack(pady=5)

# Entry (Input field)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)


# Button
tk.Button(root, text="Submit", command=show_name).pack(pady=5)

# Output Label
output_label = tk.Label(root, text="")
output_label.pack(pady=5)


# Start the GUI event loop
root.mainloop()
