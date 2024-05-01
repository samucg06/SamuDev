import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1000x500")
ventana.configure(bg="white")

frame_uno = tk.Frame(ventana)
frame_uno.configure(width=400, height=300, bg="red", bd=5)


frame_uno.pack()

ventana.mainloop()
