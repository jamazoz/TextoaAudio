import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS

try:
    os.mkdir("temp")
except:
    pass
st.title("Text to speech")

input_language="es" 
output_language="es"

text = st.text_input("Escriba el texto")

def text_to_speech(text, tld):
    #translation = translator.translate(text, src=input_language, dest=output_language)
    
    tts = gTTS(text, "es", tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text


display_output_text = st.checkbox("Muestra el  texto ")

if st.button("convert"):
    result, output_text = text_to_speech(input_language, output_language, text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown(f"## Output text:")
        st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
