# 🧠 AI Voice Agent – Development Roadmap  

## 🧭 Roadmap Summary  
This roadmap outlines **our plan for building the first multilingual AI Voice Agent from Bangladesh**.  

We’re keeping everything **realistic and flexible** — these micro-steps are **estimates**, not deadlines.  
They’ll evolve as we learn, experiment, and face real challenges during development.  

Our main goal isn’t just to finish fast — it’s to **build, test, learn, and improve continuously**.  
Every small milestone will teach us something new about **voice quality**, **Bangla/English speech understanding**, and **natural human-like interaction**.  

We want to create an AI agent that can handle **real conversations** — whether that’s confirming an e-commerce order in Bangla or setting an appointment for a clinic in English — and eventually scale this system **globally**.

---

## 🌍 Big-picture MVP (One-Sentence)
A system where a company uploads customer details → our AI automatically calls in Bangla or English → confirms details or completes a small task → saves audio + transcript → and records the outcome (confirmed / not / needs human) — all viewable from a simple dashboard or Google Sheet.

---

## ⚙️ Tech Stack (Practical + Lean)

- 📞 **Telephony:** [Twilio](https://www.twilio.com/) for outbound calls & recordings  
- 🗣️ **Speech-to-Text (STT):** OpenAI Whisper API (or local Whisper for cost-saving)  
- 🔊 **Text-to-Speech (TTS):** Coqui TTS for Bangla (local) or ElevenLabs/OpenAI for natural cloud voices  
- 🧩 **Dialog Logic:** Simple rule-based flow + optional small LLM fallback (Rasa later if needed)  
- 💾 **Storage / Dashboard:** Google Sheets or SQLite → Streamlit/React UI  
- 🖥️ **Backend:** Python (FastAPI or Flask)  
- ☁️ **Hosting:** Local dev → small VPS (DigitalOcean / Render / Railway)  
- 🔁 **Job Queue:** Simple background tasks (Celery / Redis or sequential loop)  

---

## ✅ Minimum Viable Features (MUST-HAVE)

- [x] Upload customer data (form or CSV)  
- [x] Place automated outbound calls (Bangla/English)  
- [x] Speak with natural AI voice  
- [x] Record and store every call  
- [x] Convert speech → text and save transcript  
- [x] Detect outcome (confirmed / not / human follow-up)  
- [x] Display all results in dashboard or Google Sheet  

---

## 🧱 Micro-Step Roadmap  

<details>
<summary>🚀 Sprint 0 — Setup & Planning (2–4 sessions)</summary>

- [ ] Create GitHub repo, README, and issue board  
- [ ] Set up a simple task board (Trello or GitHub Projects)  
- [ ] Assign roles (Person A & Person B)  
- [ ] Define simple wireframe & conversation flow  
- [ ] Write 4–6 sample call scripts (Bangla + English)  
- [ ] Map common responses (“Yes”, “Na”, “Hmm”)  
- [ ] Create Twilio account & get test credits  

✅ **Goal:** We have the repo, basic call scripts, and Twilio sandbox set up.
</details>

---

<details>
<summary>📂 Sprint 1 — Data Input & Storage (3–6 hrs)</summary>

- [ ] Build simple form or CSV upload option  
- [ ] Parse and store leads with fields: `id`, `name`, `phone`, `order`, `status`, `call_id`, `transcript_url`  
- [ ] Store data in Google Sheet or SQLite  

✅ **Goal:** We can upload customer data and view them easily.
</details>

---

<details>
<summary>📞 Sprint 2 — Outbound Call Skeleton (4–8 hrs)</summary>

- [ ] Connect backend to Twilio API for outbound calls  
- [ ] Build TwiML webhook to handle call logic  
- [ ] Test first live call (AI → our phone)  

✅ **Goal:** Press “Call” → AI makes real outbound call.
</details>

---

<details>
<summary>🗣️ Sprint 3 — Text-to-Speech (TTS) – Bangla & English (6–12 hrs)</summary>

- [ ] Generate voice clips using Coqui TTS (Bangla) and cloud TTS (English)  
- [ ] Test voice quality and clarity  
- [ ] Integrate TTS audio playback with Twilio  

✅ **Goal:** The AI speaks naturally in both Bangla and English.
</details>

---

<details>
<summary>🎙️ Sprint 4 — Record Call & Save Audio (2–4 hrs)</summary>

- [ ] Enable Twilio call recording  
- [ ] Store audio locally or in S3 bucket  
- [ ] Link audio files to leads in DB  

✅ **Goal:** Every call has a saved audio recording.
</details>

---

<details>
<summary>🧾 Sprint 5 — Speech-to-Text (STT) Transcription (4–8 hrs)</summary>

- [ ] Send call recordings to Whisper API for transcription  
- [ ] Save transcripts and link to leads  
- [ ] Optionally store timestamps  

✅ **Goal:** Each call has a transcript stored and searchable.
</details>

---

<details>
<summary>🧠 Sprint 6 — Conversation Logic & Result Parsing (6–10 hrs)</summary>

- [ ] Implement simple rule-based NLU (regex or keyword-based)  
- [ ] Identify “confirm”, “not confirmed”, or “ambiguous” replies  
- [ ] Save structured call outcomes  

✅ **Goal:** System automatically classifies the call result.
</details>

---

<details>
<summary>🔁 Sprint 7 — Retry Logic, Edge Cases & Logging (4–8 hrs)</summary>

- [ ] Add logic for failed/unclear calls  
- [ ] Create retry or human review rules  
- [ ] Log all API and call errors for debugging  

✅ **Goal:** Calls are reliable and error handling is solid.
</details>

---

<details>
<summary>📊 Sprint 8 — Dashboard & Notifications (6–12 hrs)</summary>

- [ ] Build simple Streamlit/React dashboard  
- [ ] Display calls, transcripts, and outcomes  
- [ ] Send SMS/WhatsApp/email notification when confirmed  

✅ **Goal:** Businesses can view and manage all call results.
</details>

---

<details>
<summary>🧩 Sprint 9 — Pilot Test & Feedback (Ongoing)</summary>

- [ ] Run 10–50 real calls with sample clients  
- [ ] Gather feedback on clarity, accuracy, and naturalness  
- [ ] Fine-tune voice, conversation flow, and NLU logic  
- [ ] Optional: Add Rasa or small LLM for better fallback responses  

✅ **Goal:** A fully working MVP tested with real users.
</details>

---

## 👥 Roles & Collaboration  

**Person A (Telephony + Integration)**  
- Twilio setup, outbound flow, recording, notifications, retry logic  

**Person B (Backend + Speech)**  
- Data handling, TTS/STT integration, transcript storage, dashboard  

We’ll switch roles occasionally to **learn both sides** of the system.  

---

## 💰 Estimated MVP Costs  

| Category | Description | Estimated Cost |
|-----------|--------------|----------------|
| ☎️ Twilio | Outbound calls, SMS | $5–$50 |
| 🧠 Whisper API | Transcription | $2–$10 |
| 🔊 Cloud TTS | Optional natural voice | $5–$20 |
| ☁️ VPS Hosting | DigitalOcean / Render | $5–$10 |
| **💵 Total (Monthly)** | **Approximate MVP Range** | **$10–$100/month** |

---

## ⚠️ Practical Tips & Lessons Learned  

- 🎯 Keep dialogues short and structured — helps AI understand better  
- 🗣️ Confirm critical info explicitly (“Just to confirm, size 42, right?”)  
- 🎧 Always record audio + logs + transcripts for debugging  
- 🧾 Be transparent about call recording (privacy compliance)  
- 🇧🇩 Include local Banglish and regional words for better NLU accuracy  

---

🚀 What We’re Doing Right Now

We’ve already set up our GitHub repo and project board.
Right now, we’re:

✍️ Writing and refining Bangla & English conversation scripts
🔍 Exploring Twilio and other possible tools for call automation
🧠 Researching which frameworks and APIs we’ll use to build our first working AI voice prototype
---

## 🌟 Final Note  

We’re building Bangladesh’s **first AI Voice Agent** — capable of understanding and speaking **Bangla naturally**, while being powerful enough to scale globally in **English and other languages**.  

This project isn’t just about automation — it’s about giving **AI a real human voice** for every business.  
Step by step, we’ll make it happen. 💪  

---

**– Mohammed Rakib & Team**
