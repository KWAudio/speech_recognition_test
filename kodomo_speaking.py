import io
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
import simpleaudio as sa

client = ElevenLabs(
    api_key="API Key"
)

def text_to_speech_play(text):
    # Convert text to speech using ElevenLabs
    response = client.text_to_speech.convert(
        voice_id="ecp3DWciuUyW7BYM7II1",#21m00Tcm4TlvDq8ikWAM
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.3, # 안정화 0.4로 하는순간 ㅄ임
            similarity_boost=0, # ㅃㄹㅃㄹ
            style=0.7, # 감정표현 정도
            use_speaker_boost=False,
        ),
    )

    # Read all chunks into a BytesIO buffer
    audio_data = io.BytesIO()
    for chunk in response:
        if chunk:
            audio_data.write(chunk)

    audio_data.seek(0)  # Reset pointer to beginning of stream

    # Load MP3 data with pydub
    audio = AudioSegment.from_file(audio_data, format="mp3")

    # Play using simpleaudio
    play_obj = sa.play_buffer(
        audio.raw_data,
        num_channels=audio.channels,
        bytes_per_sample=audio.sample_width,
        sample_rate=audio.frame_rate
    )
    play_obj.wait_done()  # Wait until playback is finished

text_to_speech_play("안녕하세요. 텍스트를 음성으로 바로 출력해보겠습니다.")
