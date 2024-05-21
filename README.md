# My-Own-AI-Using-python


This AI Personal Assistant is a Python-based project that leverages various libraries and APIs to provide a range of functionalities, including speech recognition, text-to-speech conversion, web browsing, email sending, and more.

#Features
Speech Recognition: Uses speech_recognition to recognize and process voice commands.
Text-to-Speech: Utilizes pyttsx3 to convert text to speech for voice responses.
Wikipedia Integration: Fetches and reads out summaries from Wikipedia.
YouTube Automation: Plays videos on YouTube using pywhatkit.
Web Browsing: Searches the web using pywhatkit.
WhatsApp Messaging: Sends instant WhatsApp messages.
Email Sending: Sends emails using SMTP.
Screenshot Capture: Captures and saves screenshots with pyautogui.
Music Player Control: Plays, pauses, resumes, and stops songs.
OpenAI Integration: Uses the OpenAI API to handle complex queries.



Usage
Voice Commands: The assistant listens for voice commands and performs actions based on the recognized phrases.

"What time is it?" – Tells the current time.
"What's the date?" – Tells the current date.
"Search Wikipedia for [query]" – Fetches a summary from Wikipedia.
"Play [song name] on YouTube" – Plays the specified song on YouTube.
"Send a WhatsApp message to [number]" – Sends a WhatsApp message.
"Send an email to [email]" – Sends an email to the specified address.
"Take a screenshot" – Captures and saves a screenshot.
"Play song" – Plays a song from a specified path.
"Pause song" – Pauses the currently playing song.
"Resume song" – Resumes the paused song.
"Stop song" – Stops the currently playing song.
"Remember [something]" – Stores a note.
"What did you remember?" – Reads out the stored note.
"Exit" – Exits the assistant.
Fallback to OpenAI: For commands not explicitly handled, the assistant will use the OpenAI API to generate a response.
