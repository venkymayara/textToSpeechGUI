# textToSpeechGUI
from tkinter import *
from gtts import gTTS
from playsound import playsound



# Initializing window
root = Tk()
root.geometry("350x300") 
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH")



Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="Data", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)



# Function to Convert Text to Speech in Python
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Data.mp3')
    playsound('Data.mp3')



# Function to Exit
def Exit():
    root.destroy()



# Function to Reset
def Reset():
    Msg.set("")



# Define Buttons
Button(root, font = 'arial 15 bold',text = "PLAY", width = '4', command = Text_to_speech).place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)



# method that executes when we want to run our program
root.mainloop()


