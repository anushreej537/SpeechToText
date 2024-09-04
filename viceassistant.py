import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            # agar suani diya to recognize aa jaega
            print('recognizing....')
            # jo bhi audio aaya hai wo recognize hona chiye jo hi bola hai wo data aa chuka hai
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print('Not understand')
sptext()
# # yeh function hum jo bolre hai ushe text mai convert krega
# def sptext():
#     # yha pr speech_recognition module hai jiske andar ek class hoti hai rocognitionn jo bhi hum bolte hai ushe catch krti hai hmare microphone se
#     recognizer = sr.Recognizer()
#     # jo bhi source se data aaega wo le lege hum
#     with sr.Microphone() as source:
#         # ab hme instructio n milna chiye ki kab hme bolna hai
#         print('Listening...')
#         # noise cancelation krna hai hme
#         # toh noise kiski htani hai sourse ki toh wo de dege () mai
#         recognizer.adjust_for_ambient_noise(source)
#         # yha pr listen function sunne ka kaam krega
#         audio = recognizer.listen(source)
#         # ab hum yha data ko read krege

#         # yha pr ab hum try except ka use krege agar kuch sunai dera hoga toh wo record ho jaegi aur text format mai mil jaegi otherwise nhi

#         try:
#             # agar suani diya to recognize aa jaega
#             print('recognizing....')
#             # jo bhi audio aaya hai wo recognize hona chiye jo hi bola hai wo data aa chuka hai
#             data = recognizer.recognize_google(audio)
#             print(data)
#         except sr.UnknownValueError:
#             print('Not understand')
# sptext()