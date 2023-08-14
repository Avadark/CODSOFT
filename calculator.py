import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "←":
        entry.delete(len(entry.get()) - 1)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Unique Calculator")
root.geometry("300x450")
root.configure(bg="#1E2A38")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "←"
]

r = 1
c = 0
for button_text in buttons:
    btn = tk.Button(root, text=button_text, font=("Arial", 15), padx=10, pady=10, width=5, height=2, bg="#34495E", fg="white")
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew", ipadx=5, ipady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1

for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for btn in root.winfo_children():
    btn.bind("<Button-1>", on_click)

root.mainloop()
