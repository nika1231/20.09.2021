import tkinter as tk

window = tk.Tk()

label = tk.Label(
  text = 'Sveiki!Sveiki!Sveiki!Sveiki!Sveiki!',
 foreground = 'red',
 background = 'black'
 )

labeli = tk.Label(
  text = 'Čau!',
  fg = 'red',
  bg = '#34A2FE',
  width = 10,
  height = 7
 )

label.pack()
labeli.pack()

window.mainloop()