4import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

eng = pyttsx3.init("sapi5")
voices = eng.getProperty("voices")
print(voices[1].id)
eng.setProperty("voice",voices[1].id)
eng.setProperty("rate",120)
hour = datetime.datetime.now().hour
start_and_quit_program = True


def intro():
    eng.say("how can i help you")
    eng.runAndWait()


def get_user_name():
    rr = sr.Recognizer()
    with sr.Microphone() as name:
        print("Hey Speak whats you name.....")
        eng.say("Hey Speak whats you name")
        eng.runAndWait()
        listen_user_name = rr.listen(name,timeout=4,phrase_time_limit=4)
    try:
        global user_name
        user_name = rr.recognize_google(listen_user_name,language="en-in")
        eng.say(f"Ok So Your Name is {user_name}")
        eng.runAndWait()
        print(f"Ok So Your Name is : {user_name}")

    except Exception as e:
        print("Sorry I Cant't Recognize Your Name")
        eng.say("Sorry I Cant't Recognize Your Name")
        eng.runAndWait()



def Welcome():
    if hour >= 0 and hour < 12:
        eng.say(f"Hello Good Morning {user_name},How May I Help You")
        eng.runAndWait()
    elif hour >= 12 and hour < 16:
        eng.say(f"Hello Good Afternoon {user_name},How May I Help You")
        eng.runAndWait()
    elif hour >= 16 and hour < 20:
        eng.say(f"Hello Good Evening {user_name},How May I Help You")
        eng.runAndWait()
    elif hour >= 20 and hour <= 24:
        eng.say(f"Hello Good Night {user_name},How May I Help You")
        eng.runAndWait()


def takecomm():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"i am Listening...")
        eng.say(f" am Listening")
        eng.runAndWait()
        audio = r.listen(source,timeout=7,phrase_time_limit=7)
    try:
        print("Recognizing...")
        que = r.recognize_google(audio,language="en-in")
        print(f"{user_name} :{que}\n")
    except Exception as e:
        eng.say("Sorry I Cant't Recognize please speak again")
        eng.runAndWait()
        print("Sorry I Cant't Recognize please speak again")
        print(e)
    return que

if __name__=="__main__":
    intro()
    get_user_name()
    Welcome()


    while start_and_quit_program:
        recognize_user_cmd = takecomm().lower()
        with open("notepad.txt", "a") as file1:
            file1.write(f"{user_name} said : {recognize_user_cmd} \n")

        if "fee structure" in recognize_user_cmd:
            eng.say("showing you the fee structure of saraswati college of BCA")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org/contactus")

        elif "chairman" in recognize_user_cmd:
            print("Sharad Shinde is the charirman of saraswati group of institutions")
            eng.say("Sharad Shinde is the charirman of saraswati group of institutions")
            eng.runAndWait()

        elif "principal" in recognize_user_cmd:
            print("Dr.Santosh Bothe is the principal of saraswati college of BCA and MCA")
            eng.say("Dr.Santosh Bothe is the principal of saraswati college of BCA and MCA")
            eng.runAndWait()


        elif "about saraswati collage" in recognize_user_cmd:
            eng.say("you can see all the information about mauli college of engineering here")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org/about-us")

        elif "training and placement"  in recognize_user_cmd or  "t and p"  in recognize_user_cmd :
            eng.say("Showing you the result for training and placement in saraswati college of engineering")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org/training-placements")

        elif "courses" in recognize_user_cmd:
            eng.say("Showing you the courses availabel in saraswati college of engineering")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org/items")

        elif "website" in recognize_user_cmd:
            eng.say("opening website of saraswati college of engineering for you")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org")

        elif "impulse" in recognize_user_cmd or "photos" in recognize_user_cmd or "pictures" in recognize_user_cmd or "photographs" in recognize_user_cmd :
            eng.say("showing you some of the images of saraswati college of engineering")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org/impulse2022")

        elif "placement records" in recognize_user_cmd or "placements" in recognize_user_cmd or "placement record" in recognize_user_cmd  or "placements record" in recognize_user_cmd:
            eng.say("Showing the Placement Records of saraswati college of engineering")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org/training-placements")

        elif "recruiters" in recognize_user_cmd or "placements" in recognize_user_cmd  or "creators" in recognize_user_cmd or "re creators" in recognize_user_cmd:
            eng.say("The recuiters are")
            eng.runAndWait()
            webbrowser.open("https://www.saraswaticollege.org/recruiters")

        start_and_quit_program = False
