# The code was developed based on OpenAI File Search API. The code is further revised with the help of GitHub Copilot
#pip install --upgrade openai
import streamlit as st
import openai
import os
from openai import OpenAI, AssistantEventHandler
import streamlit as st
from PIL import Image

# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Create the assistant
assistant = client.beta.assistants.create(
    name="Parks & Recreation Reservation System",
    instructions="You are a parks and recreation reservation assistant. Use your knowledge base to answer questions about the parks",
    model="gpt-4o",
    tools=[{"type": "file_search"}],  # Use 'file_search' tool type
)

# Create a vector store called "San Jose Parks & Recreations"
vector_store = client.beta.vector_stores.create(name="San Jose Parks & Recreations")

# Ready the files for upload to OpenAI
file_paths = ["pages/files/SJParks.pdf"]
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
    file=open("pages/files/SJParks.pdf", "rb"), purpose="assistants"
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


# Display chat history
# Streamlit UI
st.title("Parks & Recreations Assistant Chat Interface")
st.header("Want quick information on local parks in San Jose?")
st.image("https://lp-cms-production.imgix.net/2021-09/shutterstock_441079591.jpg?w=1440&h=810&fit=crop&auto=format&q=75")

st.subheader("Ask me anything about picnic sites, capacity, pricing, timing, or park activites.")

# Display chat history
for message in st.session_state.chat_history:
    role, content = message.split(" > ", 1)
    if role == "user":
        st.write(f"**User:** {content}")
    else:
        st.write(f"**Assistant:** {content}")

# User input
user_input = st.text_input("Ask a question:")
st.write('For example:')
st.write('Which picnic sites have a capacity of more than 50 people?')
st.write('Which parks have sports activities?')
st.write('Which parks have the most picnic tables?')

# Send message to assistant
if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(f"user > {user_input}")
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
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

