# 📌 CDP Chatbot - How-To Guide  

A chatbot that helps users find **"how-to"** answers related to **Customer Data Platforms (CDPs)**:  
- [Segment](https://segment.com/docs/?ref=nav)  
- [mParticle](https://docs.mparticle.com/)  
- [Lytics](https://docs.lytics.com/)  
- [Zeotap](https://docs.zeotap.com/home/en-us/)  

It extracts relevant information from official documentation to assist users in performing tasks within each platform.  

---

## 🚀 Installation  

### 📥 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/cdp-chatbot.git
cd cdp-chatbot
```
### 🔧 2️⃣ Install Dependencies

pip install -r requirements.txt

### 🔑 3️⃣ Set Up OpenAI API Key

Create a .env file in the project root and add your API key:

OPENAI_API_KEY=your-api-key

Alternatively, set it in your terminal:

For Linux/Mac:

export OPENAI_API_KEY="your-api-key"

For Windows (CMD):

set OPENAI_API_KEY="your-api-key"

### 🏃 Run the Chatbot

Start the FastAPI server using Uvicorn:

uvicorn main:app --reload

The server will run at: http://127.0.0.1:8000

### 📡 API Endpoints
#### Method	Endpoint	Description
POST	/query	Ask a "how-to" question 

GET	/docs/load	Load & process CDP docs 

GET	/docs/search?q=...	Search docs for answers 


