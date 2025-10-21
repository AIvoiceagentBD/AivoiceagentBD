# 🧠 AI Voice Agent — Workflow Overview

## 📋 Summary
This workflow is our **estimated foundation** for how the AI Voice Agent operates — from outbound calling to understanding customer responses.  

It’s designed to be **modular, simple, and flexible**, keeping in mind that as we progress and face **real-world challenges**, this workflow will **evolve**.  

Our mission is to create a system that can **speak, listen, and understand** Bangla and English conversations naturally, serving multiple industries like **e-commerce, healthcare, and appointment scheduling**.

---

## ⚙️ Step-by-Step Workflow

### 1. Business Uploads Customers
- Owner uploads customer info: `name`, `phone`, `order`  
- Methods: web form, CSV upload, or Google Sheet integration  

### 2. Outbound Call Triggered
- Backend (Python app) instructs a telephony service (Twilio or similar) to call the customer  
- Can be triggered automatically or manually  

### 3. Speech Generation (Text-to-Speech, TTS)
- Backend converts scripted message into **Bangla or English audio** using TTS (Coqui, Bangla TTS, or cloud TTS)  
- Twilio plays the generated audio during the call  

### 4. Customer Responds
- Customer replies via voice (e.g., জি, না, address update)  
- Conversation is recorded automatically by Twilio  

### 5. Call Recording & Audio Collection
- Service provider stores audio file after the call ends  
- Backend retrieves recording for further processing  

### 6. Transcription (Speech-to-Text, STT)
- Audio file is sent to STT engine (Whisper API, BanglaSpeech2Text)  
- Converts spoken response into **text transcript**  

### 7. AI Intent Detection & Conversation Outcome
- Backend analyzes transcript using rules or local AI model  
- Classifies response as:  
  - ✅ Confirmed  
  - ❌ Not Confirmed  
  - ⚠️ Needs Human Follow-Up  

### 8. Dashboard / Results
- Display each call outcome, transcript, and recording link  
- Can be a **simple web dashboard** or Google Sheet  

### 9. Learning & Improvement (Optional)
- Owner reviews transcripts and corrects outcomes if needed  
- System improves over time via updated rules or retraining  

---

## 🧩 Three Core Building Blocks

### 1. TTS (Text-to-Speech)
- Converts AI text prompts into **speech/audio**  
- AI “speaks” order details and questions to the customer  

### 2. STT (Speech-to-Text)
- Converts customer’s spoken replies into **text transcript**  
- Used to interpret what the customer said  

### 3. LLM (Large Language Model — “The Brain”)
- Reads transcripts, detects intent, and decides next actions  
- Determines outcome: Confirmed, Not Confirmed, Needs Human  
- Can generate next prompt, clarification, or escalation  
- Optionally adapts and learns from new data and feedback  

---

## 🔄 How They Connect (Workflow)

1. **Before the call:** LLM chooses dialogues → TTS generates voice  
2. **During the call:** Telephony plays TTS → records customer response  
3. **After the call:** STT transcribes audio → LLM analyzes transcript → updates outcome  
4. **Feedback loop:** Owner reviews results → LLM learns from corrections  

---

## 🧠 LLM Core Functions

- Controls dialogue flow after each customer response  
- Decides next prompt or when to escalate to a human  
- Orchestrates actions: mark orders, log details, send notifications, update records  
- Sends instructions to TTS/STT and backend until conversation completes  

**In short:**  
- TTS makes the agent **speak**  
- STT makes it **listen and understand**  
- LLM is the **brain** driving conversation, reasoning, and continuous improvement  

---

## ⚠️ Notes
- This workflow is **estimated** and will evolve with experience  
- Real-world challenges may require changing steps, tools, or processes  
- Our goal is to gradually make the system **robust, smart, and globally scalable**
