import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from app.config import settings

SUBJECT_BY_PURPOSE = {
    "reset_password": "Mã xác minh đổi mật khẩu Free2Do",
}


def send_otp_email(to_email: str, code: str, purpose: str) -> None:
    subject = SUBJECT_BY_PURPOSE.get(purpose, "Mã xác minh Free2Do")
    body = (
        f"Mã xác minh của bạn là: {code}\n\n"
        f"Mã có hiệu lực trong {settings.OTP_EXPIRE_MINUTES} phút. "
        f"Nếu không phải bạn yêu cầu, hãy bỏ qua email này."
    )

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = formataddr(("Free2Do", settings.SMTP_USER))
    msg["To"] = to_email

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_USER, [to_email], msg.as_string())