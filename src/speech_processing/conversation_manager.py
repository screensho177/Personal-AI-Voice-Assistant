from .text_to_speech import TTS


class ConversationManager:
    def __init__(self, assistant):
        self.assistant = assistant

    async def main(self):
        tts = TTS()

        while True:
            user_input = input("You: ")

            if not user_input.strip():
                continue

            if "goodbye" in user_input.lower():
                print("AI: Goodbye!")
                tts.speak("Goodbye!")
                break

            llm_response = self.assistant.invoke(user_input)
            print(f"AI: {llm_response}")

            if llm_response:
                tts.speak(llm_response)
