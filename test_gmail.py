from src.tools.emails.emailing_tool import EmailingTool

tool = EmailingTool(
    recipient_name="Manju",
    recipient_email="manjuj276@gmail.com",
    subject="Test from AI Assistant",
    body="If you see this, Gmail tool works!"
)

print(tool.run())
