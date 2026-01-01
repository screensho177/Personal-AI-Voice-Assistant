from src.tools.calendar.calendar_tool import CalendarTool
print(">>> CALENDAR TOOL LOADED FROM:", __file__)

tool = CalendarTool(
    event_name="Test Event",
    event_datetime="2025-01-20T15:00:00",
    event_description="Testing Google Calendar integration"
)

print(tool.run())
