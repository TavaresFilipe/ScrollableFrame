import tkinter as tk
from tkinter import ttk


class ScrollableFrame(tk.Frame):
    def __init__(self, parent=None, hscroll:bool=False, vscroll:bool=False, scrollbar_kwargs={}, **kwargs):

        # Create a master Frame
        self.master_frame = tk.Frame(parent)
        self.master_frame.grid_rowconfigure(0, weight=1)
        self.master_frame.grid_columnconfigure(0, weight=1)

        # Create a Canvas
        self.canvas = tk.Canvas(self.master_frame, **kwargs)

        super().__init__(self.canvas, bg=self.canvas["bg"])

        # Create the 2 scrollbars
        if vscroll:
            self.v_scrollbar = tk.Scrollbar(self.master_frame,
                                            orient="vertical",
                                            command=self.canvas.yview,
                                            **scrollbar_kwargs)
            self.v_scrollbar.grid(row=0, column=1, sticky="news")
            self.canvas.configure(yscrollcommand=self.v_scrollbar.set)
        if hscroll:
            self.h_scrollbar = tk.Scrollbar(self.master_frame,
                                            orient="horizontal",
                                            command=self.canvas.xview,
                                            **scrollbar_kwargs)
            self.h_scrollbar.grid(row=1, column=0, sticky="news")
            self.canvas.configure(xscrollcommand=self.h_scrollbar.set)

        # Configure the Canvas bind
        self.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")), add=True)
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind_all('<Shift-MouseWheel>', self.scroll_horizontally)

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

    def scroll_horizontally(self, event):
        self.canvas.xview_scroll(int(event.delta / 120), "units")


root = tk.Tk()
root.geometry("500x400")

main_frame = ScrollableFrame(root, bg='black', bd=1, highlightcolor='lightgreen', highlightbackground='lightgreen',
                             highlightthickness=2, vscroll=True, hscroll=True)
main_frame.pack(fill='both', expand=1)

for thing in range(100):
    tk.Button(main_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)

root.mainloop()
