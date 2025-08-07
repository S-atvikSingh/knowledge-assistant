# AI-Powered Personalized Knowledge Assistant

This is a full-stack AI-powered assistant that allows users to upload documents and ask questions, receiving intelligent, context-aware responses using OpenAI's GPT models and Pinecone vector database.

---

## Features

-  **Semantic Search** with Pinecone Vector DB
-  **Contextual Chat** using OpenAI GPT models
-  Upload and embed custom documents
-  Persistent chat memory across questions
-  Full-stack application with FastAPI backend and React frontend

---

## Project Structure

knowledge-assistant/
├── backend/
│ ├── main.py # FastAPI app
│ ├── llm_utils.py # OpenAI API logic
│ ├── pinecone_utils.py # Pinecone vector store functions
│ ├── requirements.txt # Python dependencies
│ └── .gitignore
├── frontend/
│ ├── public/
│ └── src/
│ ├── components/
│ ├── App.js
│ ├── index.js
│ └── ...
├── .gitignore
├── LICENSE
└── README.md

yaml
Copy
Edit

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/S-atvikSingh/knowledge-assistant.git
cd knowledge-assistant
2. Backend Setup (FastAPI)
a. Navigate and Install Dependencies
bash
Copy
Edit
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
b. Set Environment Variables
Create a .env file in backend/:

env
Copy
Edit
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENVIRONMENT=your-pinecone-environment
PINECONE_INDEX_NAME=your-index-name
c. Run Backend Server
bash
Copy
Edit
uvicorn main:app --reload
Backend will run at: http://localhost:8000

3. Frontend Setup (React)
a. Navigate and Install
bash
Copy
Edit
cd ../frontend
npm install
b. Start React App
bash
Copy
Edit
npm start
Frontend will run at: http://localhost:3000

Screenshots
<img width="1917" height="967" alt="image" src="https://github.com/user-attachments/assets/9063e652-0d3b-48af-8ec1-e281bff1accd" />


API Endpoints
Method	Endpoint	Description
POST	/upload	Upload and embed docs
POST	/chat	Ask a question using chat

Tech Stack
Frontend: React

Backend: FastAPI (Python)

LLM: OpenAI GPT-4 / GPT-3.5

Vector DB: Pinecone

State Mgmt: React Hooks

Others: LangChain, dotenv

To-Do 
 Add PDF & CSV support

 Deploy frontend (Vercel/Netlify)

 Deploy backend (Render/Fly.io)

 Auth (e.g., Firebase/Auth0)

 GitHub Actions for CI/CD

Author
S-atvik Singh

