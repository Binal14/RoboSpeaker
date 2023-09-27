import pyttsx3
engine = pyttsx3.init()
while True:
        msg=input("Enter what you want me to say:")
        if msg=="Q":
                engine.say("By By Friend")
                engine.runAndWait()
                break
        engine.say(msg)
        engine.runAndWait()