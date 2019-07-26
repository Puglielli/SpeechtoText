import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index =1, sample_rate = 44100, chunk_size = 1024) as source:
    print("Say something!")
    audio = r.listen(source)
    print(r.recognize_google(audio))
