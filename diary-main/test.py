import speech_recognition as sr
mic = sr.Microphone()

AI = sr.Recognizer()

with mic as audio:
    AI.adjust_for_ambient_noise(audio)
    AI_audio = AI.listen(audio)
    text = AI.recognize_google(AI_audio, language = 'en-US')
    print(text)