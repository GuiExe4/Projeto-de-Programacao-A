import tkinter as tk
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from visao.janela import JanelaPaint
from controlador.paint_controller import PaintController

def main():
    root = tk.Tk()
    view = JanelaPaint(root)
    controller = PaintController(view)
    root.mainloop()

if __name__ == "__main__":
    main()