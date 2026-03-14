from fastapi import APIRouter
from app.models.schemas import VoicesResponse, Voice

router = APIRouter(prefix="/tts", tags=["TTS"])

# Kokoro TTS available voices
KOKORO_VOICES = [
    Voice(voice_id="af_heart", name="Heart", language="en-us", gender="female"),
    Voice(voice_id="af_bella", name="Bella", language="en-us", gender="female"),
    Voice(voice_id="af_nicole", name="Nicole", language="en-us", gender="female"),
    Voice(voice_id="af_aoede", name="Aoede", language="en-us", gender="female"),
    Voice(voice_id="am_adam", name="Adam", language="en-us", gender="male"),
    Voice(voice_id="am_michael", name="Michael", language="en-us", gender="male"),
    Voice(voice_id="bf_emma", name="Emma", language="en-gb", gender="female"),
    Voice(voice_id="bf_isabella", name="Isabella", language="en-gb", gender="female"),
    Voice(voice_id="bm_george", name="George", language="en-gb", gender="male"),
    Voice(voice_id="bm_lewis", name="Lewis", language="en-gb", gender="male"),
]

@router.get("/voices", response_model=VoicesResponse)
def get_voices():
    return VoicesResponse(voices=KOKORO_VOICES)