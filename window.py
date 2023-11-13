import tkinter as tk 
import core


core_class = core.CoreInit('test.cpp', 'programize')

def run():
    core_class.run_it()


def quit_it():
    core_class.quit_it()

window = tk.Tk()

window.title('RUN IT')

run_btn = tk.Button(window , text = "Run" , command = run)
quit_btn = tk.Button(window , text = "Quit" , command = quit_it)
run_btn.pack(padx = 20 , pady = 20)
quit_btn.pack(padx = 20, pady = 25)



window.mainloop()