import os
import smtplib
from typing import Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pydantic import Field
from ..base_tool import BaseTool
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[3] / ".env"
load_dotenv(dotenv_path=env_path)


class EmailingTool(BaseTool):
    recipient_name: Optional[str] = Field(default=None)
    recipient_email: str = Field(...)
    subject: str = Field(...)
    body: str = Field(...)

    def send_email_with_gmail(self):
        try:
            sender_email = os.getenv("GMAIL_MAIL")
            app_password = os.getenv("GMAIL_APP_PASSWORD")

            if not sender_email or not app_password:
                raise ValueError("GMAIL_MAIL or GMAIL_APP_PASSWORD not set")

            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = self.recipient_email
            msg["Subject"] = self.subject
            msg.attach(MIMEText(self.body, "plain"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, self.recipient_email, msg.as_string())

            return "Email sent successfully"

        except Exception as e:
            return f"Email was not sent successfully, error: {e}"

    def run(self):
        return self.send_email_with_gmail()
