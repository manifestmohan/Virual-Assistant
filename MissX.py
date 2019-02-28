import wikipedia
import wolframalpha
import tkinter
from  tkinter import messagebox
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

app_id = "KG55H9-6WH7WL3L8W"
client = wolframalpha.Client(app_id)

engine.say('')
engine.say('Welcome this is MissX')
engine.say('How can I help you')

wd = tkinter.Tk()
wd.geometry("250x50")
wd.title('MissX')

label = tkinter.Label(wd, text="Hello,I am MissX.How may i help you?")
label.pack()

indata = tkinter.Entry(wd)
indata.pack()

def process(void):
#    print(indata.get())
    question = indata.get()
    question = question.lower()
    if  question == '':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            self.txt.SetValue(r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results")
    else:
        try:
    #        wolframalpha
            res = client.query(question)
            answer = next(res.results).text
    #        print(answer)
            engine.say('answer')
            messagebox.showinfo("Answer",answer)

        except:
    #        wikipedia
    #        print(wikipedia.summary(question))
            messagebox.showinfo("Answer",wikipedia.summary(question))
        
wd.bind('<Return>',process)   

engine.runAndWait()
wd.mainloop()


