import datetime
import text_to_speech
import webbrowser
import weather
import speech_to_text




def Action(data) :   
  
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return "My name is Virtual Assistant"
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hi,Sir How can i help you today")
        return "Hi,Sir How can i help you today"
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning sir")
        return "Good morning sir"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time)+ "Hour :",(str)(current_time.minute)+ "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return 'ok sir'
    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("spotify.com is now ready for you")
        return "spotify.com is now ready for you"
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"
    elif "weather" in user_data:
        ans = weather.Weather()
        text_to_speech.text_to_speech(ans)
        return ans
    else:
        text_to_speech.text_to_speech("Im not able to understand")
        return "Im not able to understand"
