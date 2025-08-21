from tkinter import *

window = Tk()
window.title('Атрибути')
window.geometry("300x300")

top_frame = Frame(window, bg='green', height=50)
top_frame.pack(side="top", fill="x")

top_label = Label(top_frame, text="Зверху(side='top')", bg='black', fg='white')
top_label.pack(pady=10)
#--------------------------------------
left_frame = Frame(window, bg='red', height=50)
left_frame.pack(side="left", fill="both", expand=True)

left_label = Label(left_frame, text="Ліво(side='left')", bg='black', fg='white')
left_label.pack(pady=10)
#--------------------------------------
right_frame = Frame(window, bg='purple', height=50)
right_frame.pack(side="right", fill="both", expand=True)

right_label = Label(right_frame, text="Право(side='right')", bg='black', fg='white')
right_label.pack(pady=10)
#--------------------------------------
bottom_frame = Frame(window, bg='yellow', height=50)
bottom_frame.pack(side="bottom", fill="x")

bottom_label = Label(bottom_frame, text="Низ(side='bottom')", bg='black', fg='white')
bottom_label.pack(pady=10)

window.mainloop()