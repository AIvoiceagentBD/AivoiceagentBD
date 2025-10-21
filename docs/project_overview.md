# 🇧🇩 AI Voice Agent — Multilingual & Global-ready

**An AI-powered voice agent that speaks, understands, and completes short tasks — Bangla-first, globally ready.**

Built to help businesses automate short real-world conversations (appointment scheduling, order confirmations, campaigns, follow-ups) in Bangla — and designed to scale to English and other languages for global customers.

---

## 🚀 Overview

This project started as the **first Bangla-focused conversational voice agent** in Bangladesh but is engineered to be **multilingual and scalable**. The core idea: build robust conversational primitives (telephony, STT, TTS, NLU, task handling) so anything the agent does well in Bangla will work — often even better — in English and other widely supported languages.

### Primary Use Cases:
* 🏥 **Appointment scheduling** (doctors, clinics, hospitals)
* 🛍 **Order confirmation & delivery verification** (e-commerce)
* 📣 **Outbound campaigns** and promotions (discounts, offers)
* 📞 **Customer follow-ups**, surveys, and reminders
* 🌍 **Global deployments** — English (and more) support for international clients

---

## 🧩 Core Features (MVP)

* 🗣 **Conversational Voice (Bangla-first, multilingual)** — speaks and understands Bangla; built to support English and other languages.
* 📞 **Call Automation** — outbound/inbound call handling via Twilio (or other gateways).
* 🎙 **Speech-to-Text (STT)** — converts speech into text (Whisper API / local models).
* 🔊 **Text-to-Speech (TTS)** — natural voice generation (Coqui / ElevenLabs / OpenAI TTS) for Bangla and English.
* 💬 **Intent Detection & Small Task Handling** — appointment setting, order verification, confirmations, simple transactions.
* 🧾 **Recording & Transcription** — stores audio and transcripts for QA and model improvement.
* 📋 **Dashboard / Integrations** — Google Sheet, calendar (Google Calendar), CRM hooks, and simple UI for monitoring.

---

## 🌍 Multilingual & Global Strategy

* **Bangla-first**: train & refine dialog flows on local linguistic patterns, Banglish, and regional dialects.
* **English & other languages**: reuse dialogue orchestration, business logic, and telephony integration; plug in better-supported STT/TTS models and LLM services for higher-fidelity performance.
* **Model-agnostic architecture**: swap STT/TTS/LLM providers as needed per language and region.
* **Compliance & localization**: support region-specific consent/recording rules, time zones, and phone-number routing for global deployments.

---

## 💬 Example Conversations

### 🏥 Appointment Scheduling (Clinic)

| Role | Bangla Dialogue | English Translation |
| :--- | :--- | :--- |
| **Agent** | শুভ সকাল, আমি ডা. রহমান চেম্বার থেকে রীনা বলছি। আপনি কি আগামী বৃহস্পতিবার বিকেল ৪টার অ্যাপয়েন্টমেন্টটি কনফার্ম করতে চান? | Good morning — this is Rina from Dr. Rahman’s office. Would you like to confirm your appointment on Thursday at 4 PM? |
| **Customer** | জি, সময়টা ঠিক আছে। | Yes, the time is fine. |

### 🛍 E-commerce Order Confirmation (Outbound Call)

| Role | Bangla Dialogue | English Translation |
| :--- | :--- | :--- |
| **Agent** | শুভ সকাল, আমি **X** থেকে শিরা বলছি। আপনার অর্ডার নিশ্চিত করতে একটু সময় দেওয়া যাবে? | Hello, this is Shira from X. We're calling to confirm your order. |
| **Customer** | জি। | Yes. |
| **Agent** | আপনি **মাভেরিক স্পোর্ট শু (সাইজ ৪২, কালো)** অর্ডার করেছেন। এটি কি সঠিক? | You ordered Maverick Sport Shoe (size 42, black). Is that correct? |
| **Customer** | হ্যাঁ। | Yes. |
| **Agent** | দারুণ — আপনার অর্ডারটি নিশ্চিত হলো। ইনশাআল্লাহ ৩-৪ কর্মদিবসে পৌঁছে যাবে। ধন্যবাদ। | Great—your order is confirmed. It will be delivered within 3-4 working days. Thank you. |

---

## 🏗️ Tech Stack

| Component | Technology (examples) |
| :--- | :--- |
| **Backend** | Python (FastAPI / Flask) |
| **Telephony** | Twilio / Asterisk / Local gateways |
| **Speech-to-Text** | OpenAI Whisper API / Vosk / local Whisper |
| **Text-to-Speech** | Coqui TTS / ElevenLabs / OpenAI TTS |
| **NLU / Dialog** | Rasa (rules) + LLM (fallback) / LangChain |
| **Storage** | Google Sheets / SQLite / Postgres / S3 |
| **Frontend** | Streamlit / React |
| **Hosting** | Render / Railway / DigitalOcean |
| **Version Control** | Git + GitHub |

---

## 🎯 Project Goals

1.  Deliver a reliable Bangla conversational voice agent capable of short-task completion.
2.  Make the platform multilingual and production-ready for English and other languages.
3.  Provide an affordable, scalable automation product for local and international businesses.
4.  Build a data-driven improvement loop: record → transcribe → analyze → retrain.

---

## 🧩 Roadmap (High-Level)

* [x] Draft Bangla and English scripts for key flows
* [x] Twilio outbound/inbound call testing
* [ ] Integrate Bangla TTS & Whisper STT (production)
* [ ] Implement small-task logic + simple NLU (confirm/reschedule/cancel)
* [ ] Build dashboard for call logs, playbacks, and transcripts
* [ ] Pilot with local clinic + e-commerce merchant
* [ ] Add polished English flows and multi-region telephony routing

---

## 💸 Estimated Running Cost (MVP)

| Item | Est. Cost (USD/month) | Notes |
| :--- | :--- | :--- |
| Twilio Calls | $10–$50 | per-minute charges (volume dependent) |
| Whisper API | $5–$20 | speech-to-text |
| Hosting | $5–$20 | small VPS or managed service |
| TTS | $0–$50 | Coqui = free; premium voices = paid |
| **Total (approx.)** | **$20–$140/month** | depends on scale & premium services |

---

## 🧑‍💻 Team

**Developers:**
* Mohammed Rakib
* Tahmim Mustakin

**Vision:** Build a Bangla-rooted voice AI that scales globally — offering the same or better performance in English and other languages as the product matures.

---

## 🤝 Contributions

We welcome contributions, issue reports, and collaboration. If you’re interested in **voice AI, multilingual NLP, telephony**, or deployment at scale, please fork the repo and open a PR.

---

> *“Start local. Speak Bangla. Scale global.”*
