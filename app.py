import tkinter as tk
import controller as cn

if __name__ == '__main__':
    root = tk.Tk()
    root.title('OT SE Designer')
    root.withdraw()
    app = cn.Controller(root)
    root.mainloop()