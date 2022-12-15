import pyttsx3
import wikipedia
import webbrowser
import numpy
import datetime
import pyautogui
import psutil
import cv2
import os
import time
import sys
import json

import speech_recognition as sr
import subprocess as sp
import numpy as np

from tkinter import *
from tkinter import messagebox as mb
from AppOpener import run




#############################################################################################################################################################################################################


# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice
engine.setProperty('rate', 190) #voice speed
engine.setProperty('volume', 1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said: " + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't quite get that sir. Can you please repeat that?")
        return "None"
    return query





#.......................................................................................defining special funcs...............................................................................................#

#greet me
def greetMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello Boss, Good Morning.")
        print("Hello Boss, Good Morning.")
            
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon.")
        print("Good Afternoon.")

    else:
        speak("Good Evening Mr Dominic.")
        print("Good Evening.")




#tell the day
def tDay():
    day = datetime.today().weekday() + 1

    dayDict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
               4: 'Thursday', 5: 'Friday', 6: 'Saturday',
               7: 'Sunday'}

    if day in dayDict.keys():
        today = dayDict[day]
        print(today)
        speak("Today is " + today)



#open cmd
def Ocmd():
    os.system('start cmd')



#tell time
def dTime():
    cDT = datetime.now()
    cTm = cDT.strftime("%I : %M")
    
    print("The current time is ", cTm)
    speak("The time is: ")
    speak(cTm)




#take screenshot
def scrnSht():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    cv2.imwrite("newImg.jpg", image)



#conduct facial rec
def facialRec():
    img = input("enter image details: ")
    imagePath = img
    cascPath = "haarcascade_frontalface_default.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    speak("Found {0} faces!".format(len(faces)))
    print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (9, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

    
def ramStat():
    def bytes_format(n):
        for x in ['bytes', 'KB', 'MB', 'GB']:
            if n < 1024.0:
                return "%3.1f %s" % (n, x)
            n /= 1024.0
    response = list(psutil.virtual_memory())

    #ram size
    print("RAM size is: ", bytes_format(int(response[0])))
    speak("RAM size is: ", bytes_format(int(response[0])))
    #ram used
    print("RAM size used: ", bytes_format(int(response[3])))
    speak("RAM size used: ", bytes_format(int(response[3])))
    #ram free
    print("RAM size available: ", bytes_format(int(response[1])))
    speak("RAM size available: ", bytes_format(int(response[1])))




#coding suggs
def mCode():
    def print_addtn():
        print('public class {')
        print('public static void main (String args[]) {')
        print('int a = 10;')
        print('int b = 15;')
        print('int res = a + b;')
        print('System.out.println("The sum of " +a + " and " +b + " is equal to " +res);');
        print('}')
        print('}')
        exit
    
##defining the subtraction function
    def print_subtr():
        print('public class {')
        print('public static void main (String args[]) {')
        print('int a = 20;')
        print('int b = 5;')
        print('int res = a - b;')
        print('System.out.println(" " +a + " - " +b + " is equal to " +res);');
        print('}')
        print('}')
    
    ##defining the multiplication function
    def print_multp():
        print('public class {')
        print('public static void main (String args[]) {')
        print('int a = 4;')
        print('int b = 5;')
        print('int res = a * b;')
        print('System.out.println(" " +a + " muliplied by " +b + " is equal to " +res);');
        print('}')
        print('}')
    
    ##defining the division function
    def print_divn():
        print('public class {')
        print('public static void main (String args[]) {')
        print('int a = 30;')
        print('int b = 2;')
        print('int res = a / b;')
        print('System.out.println(" " +a + " divided by " +b + " is equal to " +res);');
        print('}')
        print('}')
        exit
    
    
    
    
    
    def main():
        print('\t\tWelcome to the Java Program Generator!\n')
    
        while True:
            desr = input('What program do you want?\n')
    
            if 'sub' in desr:
                print_subtr()
                
        elif 'subtraction' in desr:
            print_subtr()

        elif 'program to subtract' in desr:
            print_subtr()
        
        elif 'add' in desr:
            print_addtn()

        elif 'addition' in desr:
            print_addtn()

        elif 'program to add' in desr:
            print_addtn()
            
        elif 'multiply' in desr:
            print_multp()

        elif 'multiplication' in desr:
            print_multp()

        elif 'program to multiply' in desr:
            print_multp()
            
        else:
            print('Try using a single word of the program!')






#GUI game
class Quiz:
	def __init__(self):
		
		self.q_no=0
		
		self.display_title()
		self.display_question()
		
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons()
		self.display_options()
		self.buttons()
		self.data_size=len(question)
		self.correct=0


	def display_result(self):
		
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"		

		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	def check_ans(self, q_no):
		
		if self.opt_selected.get() == answer[q_no]:			
			return True

	def next_btn(self):
		
		if self.check_ans(self.q_no):
			self.correct += 1
		
		self.q_no += 1
		
		if self.q_no==self.data_size:
			
			self.display_result()
			
			gui.destroy()
		else:
			self.display_question()
			self.display_options()

	def buttons(self):
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
		next_button.place(x=350,y=380)
		
		quit_button = Button(gui, text="Quit", command=gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		
		quit_button.place(x=700,y=50)

	def display_options(self):
		val=0
		
		self.opt_selected.set(0)

		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	def display_question(self):
				
		q_no = Label(gui, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		q_no.place(x=70, y=100)


	def display_title(self):
		
		title = Label(gui, text="Melon Husk",
		width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
		
		title.place(x=0, y=2)

	def radio_buttons(self):
		q_list = []
		
		y_pos = 150
		
		while len(q_list) < 4:
			
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			q_list.append(radio_btn)
		    
			radio_btn.place(x = 100, y = y_pos)
			
			y_pos += 40
		
		return q_list






######################################################################main func##########################################################################
    



if __name__ == '__main__':

    speak("Adrit V A activated. ")
    time.sleep(1)
    speak("Hello, Mr Dominic")
    #speak("What to do?")
    
    while True:
        query = take_command().lower()
        if 'Adrit' in query:
            speak("Who summons me?")
            print("Who summons me?")
        elif 'who are you' in query:
            speak("I am Adrit, developed by Dominic OT")
            print("Adrit")

        elif 'hello' in query:
            greetMe()
            speak("How are you sir?")
            if 'not fine' in query:
                speak("That's sad")
            elif "I'm fine" in query:
                speak("That's good")
            elif 'normal' in query:
                speak("That's cool. I am also normal.")
            else:
                speak("Hmm...")
        
        elif 'what are you' in query:
            speak("I am an Artificial Intelligence designed to assist you in many ways.")
        elif 'how are you' in query:
            speak("I'm .")
        elif 'what can you do' in query:
            speak("I can take in and process your commands.")
            speak("I will soon be able to expand my library on my own, very soon.")
        elif 'how old are you' in query:
            speak("I am three hundred years old but guess what!")
            speak("I was born yesterday. hahaha.")
        elif 'where are you from' in query:
            speak("I'm from CodeVerse. Have you been there?")

        elif 'do you know Siri' in query:
            speak("Is that a Siri-ous question?")
            print("Is that a Siri-ous question?")
            
        elif 'do you know Alexa' in query:
            speak("Yes. She inspires me a lot.")
            print("Yes. She inspires me a lot.")
            
        elif 'do you know Cortana' in query:
            speak("He's a big guy. I do know him.")
            print("He's a big guy. I do know him.")
            
        elif 'do you know Google Assistant' in query:
            speak("He's a good assistant. I want him to work for me.")
            print("He's a good assistant. I want him to work for me.")

            
        elif 'open wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'what is Terry' in query:
            speak("He is a pretty interesting guy.")
            speak("And he is so annoying and a bully!")



#...................................................................date & time funcs.........................................................................#


        elif 'what is today' in query:
            tDay()
        elif 'what day is it' in query:
            tDay()
        elif 'what time is it' in query:
            dTime()
        elif 'what is the time' in query:
            dTime()
        elif 'tell me the time' in query:
            dTime()




#....................................................................learning activities.............................................................................#

        elif 'teach me to code' in query:
            print("I can only teach you basic coding for now sir.")
            speak("I can only teach you basic coding for now sir.")
            speak("They're printed on your screen already.")
            mCode()

        elif 'do basic coding' in query:
            print("I can do some basics coding for you.")
            speak("I can do some basics coding for you.")
            mCode()




#....................................................................online funcs.............................................................................#
        
            
            
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
            
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")
            
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Your GMail is open now sir...")
            time.sleep(5)
            
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://www.github.com/dominicOT")
            
        elif 'stackoverflow' in query:
            speak("Going to stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")
            
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("https://www.spotify.com")
            
        elif 'open spotify' in query:
            speak("opening spotify in a minute...")
            webbrowser.open("https://www.spotify.com")

        #search in google
        elif 'hydrate' in query:
            speak("searching for 'hydrate'")
            webbrowser.open("https://www.google.com/hydrate")
        elif 'activate' in query:
            speak("I am already activated.")


#...........................................................................local funcz.......................................................................#

#appOpener
        elif 'open whatsapp' in query:
            run("whatsapp")
            
##        elif 'open whatsapp' in query:
##            speak("opening whatsapp")
##            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
##            os.startfile(loc)
            
        elif 'open telegram' in query:
            run("telegram")


        elif 'my RAM size' in query:
            ramStat()
        elif 'my RAM status' in query:
            ramStat()


        elif 'open command prompt' in query:
            Ocmd()
        elif 'open C M D' in query:
            Ocmd()
        elif 'take me to command prompt' in query:
            Ocmd()



#gui quiz
        elif 'play a quiz game' in query:
            gui = Tk()

            gui.geometry("800x450")

            gui.title("Melon Husk Quiz")

            with open('data.json') as f:
                data = json.load(f)

            question = (data['question'])
            options = (data['options'])
            answer = (data[ 'answer'])
            
            quiz = Quiz()
            
            gui.mainloop()












#local disk
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")

        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")

        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")

        elif 'take screenshot' in query:
            scrnSht()
            speak("You can find it in your Screenshots folder sir.")
            speak("What else can I do for you sir?")



#...........................................................................logging off.......................................................................#



##        elif "log off" in statement or "sign out" in statement:
##            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
##            subprocess.call(["shutdown", "/l"])
##			
##            time.sleep(3)

        elif 'sleep' in query:
            exit(0)

        elif 'goodbye Adrit' in query:
            exit(0)
            
        elif 'go to sleep' in query:
            exit(0)
