
import tkinter as tk

def hi():
    print("hi")



app = tk.Tk()


dice1_label = tk.Label(text = "Dice 1").grid(row = 1, column=0)
dice2_label = tk.Label(text = "Dice 2").grid(row = 2, column=0)
dice3_label = tk.Label(text = "Dice 3").grid(row = 3, column=0)
dice4_label = tk.Label(text = "Dice 4").grid(row = 4, column=0)
dice5_label = tk.Label(text = "Dice 5").grid(row = 5, column=0)
dice6_label = tk.Label(text = "Dice 6").grid(row = 6, column=0)

dice1_entry = tk.Label()


button = tk.Button(text ="Roll", command = hi).grid()

# active_dice = 6
# dice_labels = []
# for i in range(active_dice):
#     dice_labels.append()



app.mainloop()