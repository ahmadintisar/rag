import gradio as gr
from upload_file import UploadFile
from chatbot import ChatBot
from ui_settings import UISettings

CSS = """
/* Hide the entire footer */
footer {
    display: none !important;
}

/* Hide containers for "Use with API" or "Share" links */
.share-btn-container,
.share-link-container,
.usage-links,
.api-docs,
#share-btn,
#share-btn-container {
    display: none !important;
}

/* Hide any anchor linking to gradio.app (fallback) */
a[href*="gradio.app"] {
    display: none !important;
}

/* Attempt various fallback selectors to ensure the chatbot avatar fits */
#chatbot .avatar img,
#chatbot .avatar > img,
#chatbot .gradio-chatbot-avatar,
#chatbot .chatbot-avatar {
    width: 50px !important;
    height: 50px !important;
    object-fit: cover !important;
    border-radius: 50% !important;
}

/* Center the brand image column content */
#brand_column > .wrap {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Hide the download button for the brand image */
#branded_logo .gr-image-download-btn {
    display: none !important;
}
"""

with gr.Blocks(css=CSS, title="Demo Bot") as demo:
    with gr.Tabs():
        with gr.TabItem("Origen"):
            # ROW ONE: Brand Image (left) + Chatbot (center) + Reference Bar (hidden)
            with gr.Row():
                with gr.Column(scale=1, elem_id="brand_column"):
                    # Centered brand image on the left
                    displayed_logo = gr.Image(
                        value="images/branded_content.png",
                        label="Branded Image",
                        show_label=False,
                        interactive=False,
                        elem_id="branded_logo"
                    )

                with gr.Column(scale=2) as chatbot_output:
                    chatbot = gr.Chatbot(
                        [],
                        elem_id="chatbot",
                        bubble_full_width=True,
                        height=500,
                        avatar_images=(
                            "images/user.png",
                            "images/techbyorigen_logo.jpeg"
                        ),
                    )
                    chatbot.like(UISettings.feedback, None, None)

                with gr.Column(scale=1, visible=False) as reference_bar:
                    ref_output = gr.Markdown()

            # ROW TWO: Text input
            with gr.Row():
                input_txt = gr.Textbox(
                    lines=4,
                    scale=8,
                    placeholder="Enter text and press enter, or upload PDF files",
                    container=False,
                )

            # ROW THREE: Buttons, sliders, dropdowns
            with gr.Row():
                text_submit_btn = gr.Button(value="Submit text")
                sidebar_state = gr.State(False)
                btn_toggle_sidebar = gr.Button(value="References")
                btn_toggle_sidebar.click(
                    UISettings.toggle_sidebar,
                    [sidebar_state],
                    [reference_bar, sidebar_state]
                )
                upload_btn = gr.UploadButton(
                    "\U0001F4C1 Upload PDF or doc files",
                    file_types=['.pdf', '.doc'],
                    file_count="multiple"
                )
                temperature_bar = gr.Slider(
                    minimum=0,
                    maximum=1,
                    value=0,
                    step=0.1,
                    label="Creativity",
                    info="Choose between 0 and 1"
                )
                rag_with_dropdown = gr.Dropdown(
                    label="RAG with",
                    choices=["Upload doc: Process for RAG", "Upload doc: Give Full summary"],
                    value="Upload doc: Process for RAG"
                )
                clear_button = gr.ClearButton([input_txt, chatbot])

            # Process callbacks for Chatbot
            file_msg = upload_btn.upload(
                fn=UploadFile.process_uploaded_files,
                inputs=[upload_btn, chatbot, rag_with_dropdown],
                outputs=[input_txt, chatbot],
                queue=False
            )

            txt_msg = input_txt.submit(
                fn=ChatBot.respond,
                inputs=[chatbot, input_txt, rag_with_dropdown, temperature_bar],
                outputs=[input_txt, chatbot, ref_output],
                queue=False
            ).then(lambda: gr.Textbox(interactive=True), None, [input_txt], queue=False)

            txt_msg = text_submit_btn.click(
                fn=ChatBot.respond,
                inputs=[chatbot, input_txt, rag_with_dropdown, temperature_bar],
                outputs=[input_txt, chatbot, ref_output],
                queue=False
            ).then(lambda: gr.Textbox(interactive=True), None, [input_txt], queue=False)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))  # Default to 7860 if no PORT is set
    demo.launch(server_name="0.0.0.0", server_port=port)
