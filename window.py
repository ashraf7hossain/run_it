import tkinter as tk 
import core



class MyUI:

    def __init__(self):
        self.root = tk.Tk()

        self.core_class = None
       
        self.label = tk.Label(self.root , text = "RUN_IT", font=('Arial', 32))
        self.label.pack(padx=10,pady=10)


        self.label = tk.Label(self.root , text = "Put your file path", font=('Arial', 10))
        self.label.pack(padx=10,pady=10)

        self.text_box = tk.Text(self.root, height = 2, font=('Arial',10))
        self.text_box.pack(padx=10 ,pady=10)

        self.check_state = tk.StringVar()
        self.check_state.set("onecompiler")

        self.radio_box = tk.Radiobutton(self.root , text = "Onecompiler", font=('Arial',10),variable=self.check_state ,value = "onecompiler")
        self.radio_box.pack(padx=10,pady=10)

        self.radio_box = tk.Radiobutton(self.root , text = "Programize", font=('Arial',10),variable=self.check_state, value = "programize")
        self.radio_box.pack(padx=10,pady=10)

        self.run_btn = tk.Button(self.root , text = "Run" , font=('Arial' , 10), width=10 , command = self.run)
        self.run_btn.pack(padx=10,pady=10)

        self.quit_btn = tk.Button(self.root , text = "Quit" , font=('Arial' , 10), width=10 , command = self.quit_it)
        self.quit_btn.pack(padx=10,pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.root.mainloop()

    def run(self):
        if self.core_class != None:
            self.core_class.quit_it()
            self.core_class = None 
        
        state = self.check_state.get()
        file_path = self.text_box.get("1.0", tk.END)

        print("file path " , type(file_path), state)

        self.core_class = core.CoreInit(file_path, state)

        self.core_class.run_it()
        
        # print(self.check_state.get(), self.text_box.get("1.0",tk.END))

    def quit_it(self):
        if self.core_class:
          self.core_class.quit_it()
    def on_close(self):
        self.quit_it()
        self.root.destroy()
    

        

MyUI()
