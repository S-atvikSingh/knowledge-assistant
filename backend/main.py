# backend/main.py
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from pinecone_utils import ingest_text_to_pinecone, search_similar_documents
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print("OPENAI_API_KEY:", OPENAI_API_KEY[:5] + "..." if OPENAI_API_KEY else "OPENAI_API_KEY Not Found")

CHAT_HISTORY_FILE = "chat_history.json"

# Init FastAPI
app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
def root():
    return {"message": "Knowledge Assistant backend is live!"}

# Request schemas
class UploadRequest(BaseModel):
    text: str

class ChatRequest(BaseModel):
    query: str

def save_chat_history(user_id, user_input, bot_response):
    try:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "user_input": user_input,
            "bot_response": bot_response
        }

        try:
            with open(CHAT_HISTORY_FILE, "r") as f:
                history = json.load(f)
        except FileNotFoundError:
            print("FileNotFoundError for save chat history:", e)
            history = []
        except json.JSONDecodeError as e:
            print("Failed to decode JSON from history file:", e)
            history = []

        history.append(entry)

        with open(CHAT_HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)

        print("Chat history saved.")

    except Exception as e:
        print("Failed to save chat history:", e)


# Upload endpoint
@app.post("/upload")
async def upload_knowledge(req: UploadRequest):
    return ingest_text_to_pinecone(req.text)

from openai import OpenAI
client = OpenAI()

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # Step 1: Search Pinecone for similar documents
        docs = search_similar_documents(req.query)

        # Step 2: Combine the documents for context
        context = "\n\n".join([doc.page_content for doc in docs])

        #print("context is : "+str(context[:100]))
        # Step 3: Create the prompt for OpenAI chat
        messages = [
            {"role": "system", "content": 
             "You are a helpful assistant. Try to answer the question based on the knowledge in content. If you are making any assumptions mark them as such."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{req.query}"}
        ]

        # Step 4: Use OpenAI's updated v1 client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print("OpenAi: "+str(response))
        
        # Step 5: Extract the assistant's reply
        reply = response.choices[0].message.content.strip()
        print("Saving chat history...")
        print("User:", req.query)
        print("Bot:", reply)
        # Step 6: Save chat history (text only)
        save_chat_history(user_id="default_user", user_input=req.query, bot_response=reply)
        print("Save chat is working")
        # Step 7: Return the assistant's reply to the frontend
        return {"response": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
