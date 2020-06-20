# import các thư viện cần dùng
import speech_recognition
from gtts import gTTS
import os
# Khởi tạo
bot_brain = "" # Ban đầu chưa học gì nên não chưa có thông tin
bot_ear = speech_recognition.Recognizer() # Siri nghe

with speech_recognition.Microphone() as mic:
    print("\nSiri: I'm listening")
    audio = bot_ear.record(mic, duration=3)
    # Siri nghe trong vòng 3 giây sau đó tắt Mic, tránh treo máy do bật Mic lien tục
    print("\nSiri: ....")
try:
    you = bot_ear.recognize_google(audio, language='vi-VN')
    # nó sẽ lấy giọng của chị Google
    print("\nYou: "+you)
except:
    you = "Tôi không hiểu bạn nói gì."
    print("\nSiri: "+you)

you = you.lower()

if "Xin chào" in you:
    bot_brain = "Xin chào Châm"
elif "thời tiết" in you:
    bot_brain = " Hôm nay trời nhiều mây"
elif "thứ " in you:
    bot_brain = "Thứ 7 ngày 20 tháng 6 năm 2020"
elif "bye" in you:
    bot_brain = "Chào tạm biệt và hẹn gặp lại."
elif "yêu" in you:
    bot_brain = "Người yêu của Châm là Hằng, biệt danh là chó con."

else:
    bot_brain = " Cảm ơn bạn"
    print("\nSiri: " + bot_brain)
print("\nSiri: " + bot_brain)

tts = gTTS(text=bot_brain, lang='vi')
tts.save("Siri.mp3")
os.system("afplay Siri.mp3")