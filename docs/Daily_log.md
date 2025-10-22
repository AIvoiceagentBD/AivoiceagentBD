# Daily Log: 2025-10-22

## Twilio Integration
- **Set up Twilio account**  
  Registered, verified, and configured trial account for outbound calls.
- **Obtained Twilio phone number**  
  Activated trial phone number for API usage.
- **Wrote initial Python script for outbound calls**  
  Implemented and tested code to initiate calls using Twilio’s APIs.
  > _Note:_ Source code is included in my tests folder repo (not repeated here).
- **Explored Twilio XML and platform features**  
  Learned basics of Twilio Markup Language (TwiML), its usage in call flows, and available programmable features.
- **Trial Limitations Encountered**  
  All outbound calls were unsuccessful due to trial limitations:
  - On call pickup, a trial script played requiring keypress confirmation.
  - Despite pressing keys, calls hung up, preventing code execution.

## Lead Upload Website
- **Built a single-page site for lead/order data entry**  
  Features:
  - Supports single and bulk (CSV) entry of customer orders/leads.
  - Responsive design using TailwindCSS, client-side validation.
  - CSV upload with required columns, sample CSV template download.
  - Admin dashboard for filtering/searching leads.
  - Connected to Firestore backend for data persistence.
  - Implements CRUD for leads; status toggle and delete actions.
- **Learned about required CSV format & error handling**  
  Ensured CSV headers matched framework requirements, implemented row skipping logic.

---

*Log prepared for `daily-log/2025-10-22.md`  
