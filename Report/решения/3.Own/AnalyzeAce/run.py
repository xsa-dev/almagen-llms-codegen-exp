import gradio as gr
import analyzeace.shared as shared
from analyzeace import AnalyzeAce

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(height="800px")
    msg = gr.Textbox()
    run = gr.Button("Run Test Task")
    send = gr.Button("Send")
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def process_task(user_message, history):
        shared.main()


    runner = AnalyzeAce()

    send.click(user,[msg, chatbot],[msg, chatbot],queue=False,).then(runner.run, chatbot, chatbot)
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(runner.run, chatbot, chatbot)
    run.click(process_task, [msg, chatbot], [msg, chatbot], queue=False)
    send.click(lambda: None, None, chatbot, queue=False)
    clear.click(lambda: None, None, chatbot, queue=False)


demo.queue()
if __name__ == "__main__":
    demo.launch()
