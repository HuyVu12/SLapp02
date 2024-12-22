import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyDiirIJ6bS9Ou6m09kC8dPpe3Ye9ddM6Ss')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

def genAI(prompt, history = []):
    chat_session = model.start_chat(
      history = history
    )
    response = chat_session.send_message(prompt)
    return response.text
