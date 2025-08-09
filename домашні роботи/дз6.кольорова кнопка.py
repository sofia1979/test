hexColor = ['#F61111', '#F67411', '#F69E11', '#F6DF11', '#F6DF11', '#B2F611', '#78F611', '#11F623', '#11F687', '#11F6AA', '#11F6D3', '#11E3F6', '#11C5F6', '#1183F6', '#2711F6', '#7411F6', '#B211F6', '#DB11F6', '#F611DF', '#F611A2', '#F61170', '#F61136', '#F61111', '#020202', '#FFFAFA',]

import random
from tkinter import *

wikno = Tk()
wikno.title('Кольорова рамка')
wikno.geometry('500x500')

def RandomColorFrame():
    color = random.choice(hexColor)
    frame.config(bg=f'{color}')


frame = Frame(wikno, bd=5, bg='black')

button = Button(frame, text='натисни', command=RandomColorFrame, padx=50, pady=50, font=('Arial, 30'), fg='green', bg='grey')
frame.pack()
button.pack(pady=70, padx=70)

wikno.mainloop()