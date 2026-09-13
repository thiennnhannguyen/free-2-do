import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app import models
from app.config import settings

def generate_and_save_otp(db: Session, email: str, purpose: str) -> str:
    code = f"{random.randint(0, 999999):06d}"
    now = datetime.utcnow()

    otp = models.OtpCode(
        email=email,
        code=code,
        purpose=purpose,
        expires_at=now + timedelta(minutes=settings.OTP_EXPIRE_MINUTES),
        is_used=False,
        created_at=now,
    )
    db.add(otp)
    db.commit()
    return code

def verify_otp(db: Session, email: str, code: str, purpose: str) -> bool:
    now = datetime.utcnow()

    otp = (
        db.query(models.OtpCode)
        .filter(
            models.OtpCode.email == email,
            models.OtpCode.code == code,
            models.OtpCode.purpose == purpose,
            models.OtpCode.is_used == False,  # noqa: E712
            models.OtpCode.expires_at >= now,
        )
        .order_by(models.OtpCode.created_at.desc())
        .first()
    )

    if not otp:
        return False

    otp.is_used = True
    db.commit()
    return True