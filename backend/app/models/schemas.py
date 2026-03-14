from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# ─── AUTH SCHEMAS ───────────────────────────────────────────

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: str
    email: str

# ─── TTS SCHEMAS ────────────────────────────────────────────

class TTSRequest(BaseModel):
    text: str
    voice_id: str
    language: str = "en-us"
    speed: float = 1.0

class TTSResponse(BaseModel):
    job_id: str
    status: str
    message: str

class JobStatusResponse(BaseModel):
    job_id: str
    status: str        # pending, processing, completed, failed
    audio_url: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None

# ─── VOICE SCHEMAS ──────────────────────────────────────────

class Voice(BaseModel):
    voice_id: str
    name: str
    language: str
    gender: str
    preview_url: Optional[str] = None

class VoicesResponse(BaseModel):
    voices: list[Voice]

# ─── HISTORY SCHEMAS ────────────────────────────────────────

class HistoryItem(BaseModel):
    job_id: str
    text: str
    voice_id: str
    language: str
    status: str
    audio_url: Optional[str] = None
    created_at: datetime

class HistoryResponse(BaseModel):
    items: list[HistoryItem]
    total: int