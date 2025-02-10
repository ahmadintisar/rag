import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

def transcribe_audio(audio_file):
    client = speech.SpeechClient()
    with open(audio_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ur-PK"  
    )

    response = client.recognize(config=config, audio=audio)
    transcripts = [result.alternatives[0].transcript for result in response.results]
    return transcripts

def translate_text(text, target_language="en"):
    client = translate.Client()
    translation = client.translate(text, target_language=target_language)
    return translation["translatedText"]


if __name__ == "__main__":
    video_audio_file = "path/to/your/video_audio.wav"  
    urdu_transcripts = transcribe_audio(video_audio_file)
    english_transcripts = [translate_text(transcript) for transcript in urdu_transcripts]
    for transcript in english_transcripts:
        print(transcript)
