import openai
from openai import OpenAI
import os
import base64
import requests
import streamlit as st
import os
from openai import OpenAI, AssistantEventHandler

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

uploaded_file = st.file_uploader("Choose a picture file", type=["png", "jpg", "jpeg"])

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

os.makedirs('images', exist_ok=True)

def photo_rec(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is the name of the park in the image?"},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )
    return response.choices[0].message.content


if uploaded_file is not None:
    with open(os.path.join('images',uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success("Saved File:{} to images".format(uploaded_file.name))
    image_path = os.path.join('images',uploaded_file.name)
    st.image(image_path)
    content = photo_rec(image_path)
    st.write(content)

assistant = client.beta.assistants.create(
    name="Parks & Recreation Reservation System",
    instructions="You are a parks and recreation reservation assistant. Use your knowledge base to answer questions about the parks",
    model="gpt-4o",
    tools=[{"type": "file_search"}],  # Use 'file_search' tool type
)

# Create a vector store called "San Jose Parks & Recreations"
vector_store = client.beta.vector_stores.create(name="San Jose Parks & Recreations")

# Ready the files for upload to OpenAI
file_paths = ["pages/files/SJ_Parks_Rec_Info.pdf"]
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

# You can print the status and the file counts of the batch to see the result of this operation.
print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

# Upload the user provided file to OpenAI
message_file = client.files.create(
    file=open("pages/files/SJ_Parks_Rec_Info.pdf", "rb"), purpose="assistants"
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input(f"What would you like to know about this park or rec center?")

# Send message to assistant
if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(f"user > {user_input} about {content}")
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{user_input} about {content}",
                }
            ]
        )

        class EventHandler(AssistantEventHandler):
            def on_text_created(self, text) -> None:
                st.session_state.chat_history.append(f"assistant > {text}")

            def on_tool_call_created(self, tool_call):
                pass  # No file search tool used here

            def on_message_done(self, message) -> None:
                # print a citation to the file searched (not applicable)
                st.text(message.content[0].text.value)  # Only display response

        # Then, we use the stream SDK helper
        # with the EventHandler class to create the Run
        # and stream the response.
        with client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=assistant.id,  # Assuming the assistant already exists
            instructions="Please address the user as Jane Smith. The user has a premium account.",
            event_handler=EventHandler(),
        ) as stream:
            stream.until_done()