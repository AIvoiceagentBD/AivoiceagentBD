# 🗣️ AI Voice Agent - Sample Call Script (Bangla + English)

## 🎯 Purpose
Confirming an e-commerce order through an automated Bangla/English voice agent.

---

## 📞 Call Flow

### 1. Greeting
**Agent (Bangla):** শুভ সকাল, আমি [Company Name] থেকে দিয়া বলছি। আশা করি ভালো আছেন। আপনার অর্ডার নিশ্চিত করতে একটু সময় দেওয়া যাবে?
**Agent (English):** Good morning, this is Diya from [Company Name]. I hope you're doing well. May I take a moment to confirm your order?

---

### 2. Product Details
**Agent (Bangla):** ধন্যবাদ। আপনি মাভেরিক স্পোর্ট শু (সাইজ ৪২, কালো) অর্ডার করেছেন। এটি কি সঠিক?
**Agent (English):** Thank you. You have ordered the Maverick sport shoes (Size 42, Black). Is that correct?

### 3. Order Details 
**Agent (Bangla):** ঠিক আছে, আপনার অর্ডারটি ক্যাশ অন ডেলিভারিতে, মোট মূল্য ১৫৮০ টাকা (ডেলিভারি চার্জসহ)। মূল্যটি ডেলিভারি মানকে পরিষদ করতে হবে।
**Agent (English):** Alright, your order is set for Cash on Delivery, with a total amount of 1,580 BDT (including delivery charges). The payment must be made to the delivery agent.

### 4. Order Details 
**Agent (Bangla):** ধন্যবাদ। আপনার ডেলিভারির ঠিকানা দিয়েছেন: চট্টগ্রামের আগ্রাবাদ। ঠিকানায় কোনো পরিবর্তন করতে চান?
**Agent (English):** Thank you. Your delivery address is: Agrabad, Chattogram. Would you like to make any changes to the address?

### 5. Order Details  
**Agent (Bangla):** দারুণ! আপনার অর্ডারটি নিশ্চিত হলো। ইনশাআল্লাহ, ৩-৪ কর্মদিবসের মধ্যেই আপনার অর্ডার হাতে পৌঁছে যাবে। আমাদের সঙ্গে থাকার জন্য এবং X-কে বেছে নেওয়ার জন্য আন্তরিক ধন্যবাদ। আপনার সন্তুষ্টিই আমাদের সাফল্য!
**Agent (English):** Wonderful! Your order has been confirmed. It will reach you within 3–4 working days. Thank you for staying with us and choosing X. Your satisfaction is our success!

---

### 3. Customer Possible Replies (Mapped)

## 📞 Call Flow Categories

### 1. Greeting & Answering the Call
| Intent              | Possible Responses (Bangla)            | Possible Responses (English)                       |
|---------------------|----------------------------------------|----------------------------------------------------|
| Greeting / Answer   | হ্যালো                                 | Hello (Universal, all settings, customer/agent)     |
| Greeting / Answer   | আসসালামু আলাইকুম                       | Assalamu alaikum (Formal/respectful, Muslim)      |
| Greeting / Answer   | নমস্কার                                | Nomoskar (Formal/neutral, polite, Hindu/elderly)     |
| Greeting / Answer   | বলুন                                   | Bolun (Go ahead, informal, very common)             |
| Greeting / Answer   | জি বলছেন?                              | Ji bolchen? (Yes, who is speaking?, polite urban)  |
| Greeting / Answer   | কে বলছেন?                              | Ke bolchen? (Who is speaking?, casual)             |
| Greeting / Answer   | হ্যাঁ বলুন / হুম বলুন                      | Hyaan bolun / Hum bolun (Yes, go ahead, friendly)    |
| Greeting / Answer   | আমি বলছি                               | Ami bolchi ("I'm speaking," confirming identity)   |
| Greeting / Answer   | আপনি কার সাথে কথা বলছেন?               | Apni kar shathe kotha bolchen? (Who are you calling?)|

---

### 2. Confirming the Order
| Intent              | Possible Responses (Bangla)            | Possible Responses (English)                        |
|---------------------|----------------------------------------|-----------------------------------------------------|
| Confirm Order       | হ্যাঁ ঠিক আছে                          | Yes, that's fine/OK                                  |
| Confirm Order       | জি, অর্ডার কনফার্ম                     | Yes, order confirmed                                 |
| Confirm Order       | ঠিক আছে, পাঠান                         | Okay, proceed/send                                |
| Confirm Order       | ঠিক আছে, ডেলিভারি দিন                  | Okay, deliver it                                   |
| Confirm Order       | তা দিন / দেন                           | Please give/supply it                              |
| Confirm Order       | নিশ্চিত করছি                          | Confirming                                           |
| Confirm Order       | ওকে / ঠিক আছে                          | OK / Fine                                         |
| Confirm Order       | আমি কনফার্ম করছি                       | I confirm                                          |
| Confirm Order       | আমি অর্ডার করেছি                       | I have ordered                                      |
| Confirm Order       | হ্যাঁ, আমিই অর্ডার করেছি                | Yes, I ordered                                       |
| Confirm Order       | ঠিকঠাক আসে তো?                         | Is it correct/right?                              |
| Confirm Order       | ডেলিভারির সময় জানাবেন                  | Please let me know the delivery time                |

### 3. Denying, Refusing, or Cancelling
| Intent              | Possible Responses (Bangla)            | Possible Responses (English)                      |
|---------------------|----------------------------------------|---------------------------------------------------|
| Cancel / Refuse     | না দরকার নাই                           | No, not needed                                     |
| Cancel / Refuse     | আমি এই অর্ডার করিনি                     | I didn’t order this                               |   
| Cancel / Refuse     | এইটা আমি দিই নাই                        | I didn’t place this order                        |
| Cancel / Refuse     | না, আমি অর্ডার দিই নাই                  | No, I didn’t order                                 |
| Cancel / Refuse     | ক্যান্সেল করেন                         | Please cancel                                        |
| Cancel / Refuse     | আমার লাগবে না                          | I don’t need it                                    |
| Cancel / Refuse     | না, দরকার নেই                          | No, not required                                    |
| Cancel / Refuse     | অর্ডার বাতিল করুন                       | Please cancel the order                             |
| Cancel / Refuse     | ভুল করে কল করেছেন মনে হয়                | I think you called by mistake                    |
| Cancel / Refuse     | আমি পরে অর্ডার করব                     | I’ll order later                                   |
| Cancel / Refuse     | এই মুহূর্তে দরকার নাই                   | Don’t need it now                                    |
| Cancel / Refuse     | অর্ডার ভুলে যান                         | Forget the order                                     |
| Cancel / Refuse     | আমার কনফার্ম না                        | I didn’t confirm                                     |
| Cancel / Refuse     | তা লাগবে না, ধন্যবাদ                    | No need, thank you                                   |

---

### 4. Asking for Clarification
| Intent              | Possible Responses (Bangla)            | Possible Responses (English)                          |
|---------------------|----------------------------------------|------------------------------------------------------|
| Clarify             | কোন অর্ডার?                            | Which order?                                         |
| Clarify             | কে বলছেন?                             | Who is speaking?                                     |
| Clarify             | অর্ডার নাম্বার বলুন                        | Tell me the order number                             |
| Clarify             | আপনি কোন কোম্পানি থেকে?              | Which company are you from?                          |
| Clarify             | কী প্রোডাক্টের অর্ডার?                     | Which product order?                                 |
| Clarify             | আপনি কোথা থেকে বলছেন?               | Where are you calling from?                          |
| Clarify             | বিস্তারিত বলুন                            | Please explain in detail                             |
| Clarify             | কি তথ্য লাগবে?                          | What info is needed?                                 |
| Clarify             | দয়া করে আবার বলুন                     | Please repeat                                        |
| Clarify             | ঠিক বুঝিনি, আবার বলুন                  | Didn’t catch that, please repeat                     |
| Clarify             | কোন ঠিকানায় পাঠাবেন?                  | To which address will you send?                      |
| Clarify             | ডেলিভারি কবে হবে?                      | When will delivery be?                               |

---

### 5. Ending the Call Politely
| Intent              | Possible Responses (Bangla)            | Possible Responses (English)                          |
|---------------------|----------------------------------------|------------------------------------------------------|
| End Call            | ঠিক আছে, ধন্যবাদ                      | Okay, thank you                                      |
| End Call            | আচ্ছা ভাই, ধন্যবাদ                      | Alright brother, thank you                           |
| End Call            | আপনাকেও ধন্যবাদ                      | Thank you too                                        |
| End Call            | ভালো থাকবেন                          | Stay well / Take care                                |
| End Call            | আচ্ছা, দেখা হবে                        | Okay, see you again                                  |
| End Call            | ধন্যবাদ, আল্লাহ হাফেজ                   | Thank you, Allah Hafez                               |
| End Call            | তাহলে পরে কথা হবে                     | Will talk later                                      |
| End Call            | আচ্ছা, কল রাখছি                        | Okay, ending call                                    |
| End Call            | Thanks                                 | Thanks (Banglish, urban)                             |
| End Call            | আপনি ভালো থাকুন                       | You stay well                                        |
| End Call            | যদি কিছু দরকার হয় জানাবেন               | Let me know if you need anything                     |
| End Call            | পুনরায় যোগাযোগ করব                     | I’ll contact again                                   |
| End Call            | ঠিক আছে, সুন্দর দিন কাটুক                | Have a nice day                                      |
| End Call            | বিদায়                                    | Goodbye                                              |

---

### 6. Common Connection / Issues Phrases
| Intent              | Possible Responses (Bangla)            | Possible Responses (English)                         |
|---------------------|----------------------------------------|------------------------------------------------------|
| Connection Issue    | একটু অপেক্ষা করুন                      | Please hold on                                       |
| Connection Issue    | লাইনটা কেটে গেছে                       | The line got disconnected                            |
| Connection Issue    | শুনতে পাচ্ছি না                          | Can’t hear you                                       |
| Connection Issue    | নেটওয়ার্ক প্রবলেম হচ্ছে                    | Network problem                                      |
| Connection Issue    | আপনার আওয়াজ আসছে না                | Your voice is not clear                              |
| Connection Issue    | পরে কল করছি                           | Calling again later                                  |

---

### 7. Mixed Banglish Real-life Phrases
| Intent              | Possible Responses (Bangla-English Mix) | Possible Responses (English)                         |
|---------------------|-----------------------------------------|------------------------------------------------------|
|Confirm Order        | OK, order confirm                       | Order confirmed                                      |
| Question            | Delivery ta kobe ashbe?                 | When is the delivery coming?                         |
| Cancel / Refuse     | Order ta cancel korte bolsi             | I told you to cancel the order                       |
| Confirm Order       | Order ta thik ache                      | The order is fine/confirmed                          |
| Question            | Ami ekhon bujhte parchhi na, pore call korben? | I can’t understand now, can you call later?   |
| Question            | Tracking number dile bhalo hoi          | Please give the tracking number                      |
| Confirm Order       | Same address-e pathaben                 | Send to the same address                             |
| Confirm Order       | Payment delivery te hobe                | Payment will be at delivery                          |
| Modify Order        | Product ta change korte chai            | I want to change the product                         |

---

### 4. Agent Response Based on Intent

- **If Confirmed:**  
  **Agent:** ধন্যবাদ! আপনার অর্ডারটি কনফার্ম করা হয়েছে। খুব শিগগিরই ডেলিভারি পাঠানো হবে।  
  *(Thank you! Your order has been confirmed. Delivery will be sent soon.)*

- **If Not Confirmed:**  
  **Agent:** ঠিক আছে, আপনার অর্ডারটি cancel করা হলো। ধন্যবাদ সময় দেওয়ার জন্য।  
  *(Okay, your order has been canceled. Thank you for your time.)*

- **If Unclear:**  
  **Agent:** দুঃখিত, বুজতে পারিনি, আপনি কি অর্ডারটি কনফার্ম করতে চান?  
  *(sorry I didn’t catch that. Would you like to confirm the order?)*

---

### 5. Closing
**Agent (Bangla):** আমাদের সঙ্গে থাকার জন্য এবং X-কে বেছে নেওয়ার জন্য আন্তরিক ধন্যবাদ। আপনার সন্তুষ্টিই আমাদের সাফল্য!
**Agent (English):** Thank you for staying with us and choosing X. Your satisfaction is our success!
