import tkinter as tk
from gui.main_gui import PHEVGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = PHEVGUI(root)

    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nPHEV Assistant closed by user.")
        root.destroy()


