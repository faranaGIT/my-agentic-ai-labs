import gradio as gr
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# here is the function that will be called when the user sends a message

def chat_response(message, history):
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role": "user", "content": message}],
        temperature=0.8
    )
    return response.choices[0].message.content
# here is the gradio interface that will be used to interact with the model

with gr.Blocks(theme="soft") as demo:
    gr.ChatInterface(
        title="Simple Chat Assistant",
        description="A basic gradio chat interface example",
        examples=["Tell me a joke", "Give me a motivational quote of the day", "How are you?"],
        fn=chat_response
    )

if __name__ == "__main__":
    demo.launch(share=True)
    