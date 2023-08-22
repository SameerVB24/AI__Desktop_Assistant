import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        
    else:
        speak("Good Evening")
    
    speak("I am Jarvis Sir. Please tell me How may I help you")
    
def takeCommand():
        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1 
        audio = r.listen(source)
       
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        
        print("Say that again please...")
        return "None"
    return query


    
    
if __name__ == "__main__":
    wishMe()
    data = True
    while data:
        query =takeCommand().lower() 
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Alright!..")
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
              
        elif 'how are you' in query:
            speak("I am Great Sir!. How about you?")
        
        elif 'tell me about yourself' in query:
            speak("My self Jarvis.My goal is to make people smart and provide them with instant and accurate results. I take the voice input and converts it into a computer-readable language that can answer their questions. My goal of this service is to provide users with results that they have asked for through the web")
                    
        elif 'open google' in query:
            webbrowser.open("google.com")
            
     
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime} ") 
            
            
            
        elif 'open code' in query:
            codePath = "C:\\Users\\Sameer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
            
        elif 'exit' in query:
            speak('Quitting Sir!. Thankyou for your time')
            data = False
        
            
            
        