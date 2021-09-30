import tkinter as tk
from tkinter import ttk


class ScrollableFrame(tk.Frame):
    def __init__(self, parent=None, **kwargs):
        # Create an external Frame
        self.master_frame = tk.Frame(parent)
        self.master_frame.grid_rowconfigure(0, weight=1)
        self.master_frame.grid_columnconfigure(0, weight=1)

        # Create a Canvas
        self.canvas = tk.Canvas(self.master_frame, **kwargs)

        super().__init__(self.canvas, bg=self.canvas["bg"])

        # Add a Scrollbar to the Canvas
        self.scrollbar = tk.Scrollbar(self.master_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="news")

        # Configure the Canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")), add=True)
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        # Create another frame INSIDE the Canvas
        self.canvas.create_window((0, 0), window=self, anchor="nw")
        self.canvas.grid(row=0, column=0, sticky="news")

        self.pack = self.master_frame.pack
        self.grid = self.master_frame.grid
        self.place = self.master_frame.place
        self.pack_forget = self.master_frame.pack_forget
        self.grid_forget = self.master_frame.grid_forget
        self.place_forget = self.master_frame.place_forget

    def on_mouse_wheel(self, event):
        # -1 is for direction inversion
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


root = tk.Tk()
root.geometry("500x400")

main_frame = ScrollableFrame(root, bg='black', bd=1, highlightcolor='lightgreen', highlightbackground='lightgreen',
                             highlightthickness=2)
main_frame.pack(fill='both', expand=1)

for thing in range(100):
    tk.Button(main_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)

root.mainloop()
