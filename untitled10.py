from tkinter import*
import random

root= Tk()
root.title("Testing Random Functions")
root.geometry("500x500")

guessed_password_label= Label(root)
generated_password_label= Label(root)
input_password= Entry(root)


array_3d= [[["i","j","k","l","m","n","o","p"],["King","Queen"],["!","@","#","$","%","&","^","*"]]]
print(array_3d[0][2][3])

def newPassword():
    guessed_password_label["text"]= "guessed password:" + input_password.get()
    
    random_number_1= random.randint(0,5)
    random_number_2= random.randint(0,1)
    random_number_3= random.randint(0,7)
    letter_1= array_3d[0][0][random_number_1]
    letter_2= array_3d[0][1][random_number_2]
    letter_3= array_3d[0][2][random_number_3]
    guessed_password_label["text"]= "generated password:" +  letter_1+ " " + letter_2 + " " + letter_3
    
btn= Button(root,text="New Password", command= newPassword)
btn.place(relx=0.5,rely=0.5, anchor= CENTER)

input_password.place(relx=0.5, rely=0.3, anchor= CENTER)
guessed_password_label.place(relx=0.5, rely=0.4, anchor= CENTER)
generated_password_label.place(relx=0.5, rely=0.6, anchor= CENTER)

    

root.mainloop()
    