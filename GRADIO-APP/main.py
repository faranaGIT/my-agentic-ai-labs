import gradio as gr
import requests

def chat_response(message, history):
    try:
        result = requests.post(
            'http://localhost:8000/generate',
            json={"message": message}
        )
        result.raise_for_status()
        return result.json().get("message", "No 'response' recieved")
    except requests.exceptions.RequestException as e:
        return f"Error connecting server: {e}"

with gr.Blocks(theme="soft") as demo:
    gr.ChatInterface(
        title="Simple Chat Assistant",
        description="A basic gradio chat interface example",
        examples=["Tell me a joke", "Give me a motivational quote of the day", "How are you?"],
        fn=chat_response
    )

if __name__ == "__main__":
    demo.launch(share=True)

