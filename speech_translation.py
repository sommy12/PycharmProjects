#language translator algorithm


import pyttsx3 as tts
from googletrans import Translator
import googletrans as gt, moviepy as mp
import speech_recognition as sr

try:
    from_lang = str(input('[input user language]:'))
    to_lang = str(input('[input destination language]:'))
    voice_int = int(input('[speech output voice]:'))

    chinese_lang = 'zh-cn'
    english = 'en'
    french = 'fr'
    korean = 'ko'
    italian = 'it'
    dutch = 'nl'
    german = 'de'

    try:


        # converting video to audio format or changing from one audio/video format to the other
        #clip = mp.VideoFileClip("Python Tutorial.MP4")
        #clip.audio.write_audiofile("converted.wav")

        #converting speech to text algorithm
        r = sr.Recognizer()

        print('[Detecting Audio...] \n')
        with sr.Microphone() as source:
            print('[Speak Into System Microphone...] \n')
            r.adjust_for_ambient_noise(source)
            audio_text = r.listen(source)
            print('[Audio Detected...] \n')

            try:
                print('[Converting Audio Transcript Into Text...] \n')
                text = r.recognize_google(audio_text, language=from_lang)
                print('[Text:] ' + text + '\n')

            except Exception as err:
                print('Error:', err)
    except Exception as err:
        print('Error:', err)


    #try:
    #
    #
    #    # converting video to audio format or changing from one audio/video format to the other
    #    #clip = mp.VideoFileClip("Python Tutorial.MP4")
    #    #clip.audio.write_audiofile("converted.wav")
    #
    #    #converting speech to text algorithm
    #    r = sr.Recognizer()
    #
    #    print('[Detecting Audio...] \n')
    #    with sr.AudioFile('speech-to-text.wav') as source:
    #        print('[Audio Detected...] \n')
    #        r.adjust_for_ambient_noise(source)
    #        audio_text = r.record(source, duration=60)
    #
    #        try:
    #            print('[Converting Audio Transcript Into Text...] \n')
    #            text = r.recognize_google(audio_text, language="en-EN")
    #            print('[Text:] ' + text + '\n')
    #
    #        except Exception as err:
    #            print('Error:', err)
    #except Exception as err:
    #    print('Error:', err)


    #translating from one language to another
    ts = Translator()
    file = gt.LANGUAGES
    #print(file)
    print(ts.detect(f"[Detected: {text}] \n"))
    new_text = ts.translate(text, src=from_lang, dest=to_lang)
    print("[Translated text:]" + new_text.text, "\n")

    #voice0 = english(male)
    #voice1 = english(female)
    #voice2 = french
    #voice3 = italian
    #voice4 = korean
    #voice3 = chinese

    #converting translated text back to speech
    engine = tts.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[voice_int].id)
    engine.say(new_text.text)
    engine.runAndWait()

except Exception as error:
    print('Error:', error)



