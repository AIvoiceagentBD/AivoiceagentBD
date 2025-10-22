# 🗣️ AI Voice Agent - Sample Call Script (Bangla + English)

## 🎯 Purpose
Confirming an e-commerce order through an automated Bangla/English voice agent.

---

## 📞 Call Flow

### 1. Greeting
**Agent (Bangla):** হ্যালো, আমি [Company Name] থেকে বলছি। আপনি কি [Customer Name] বলছেন?  
**Agent (English):** Hello, this is [Company Name]. Am I speaking with [Customer Name]?

---

### 2. Order Confirmation
**Agent (Bangla):** আপনি আমাদের কাছে [Product Name] এর অর্ডার করেছিলেন। আপনি কি এখনো অর্ডারটি কনফার্ম করতে চান?  
**Agent (English):** You placed an order for [Product Name]. Would you like to confirm this order?

---

### 3. Customer Possible Replies (Mapped)

| Intent | Possible Responses (Bangla) | Possible Responses (English) |
|--------|-----------------------------|-------------------------------|
| ✅ Yes / Confirm | "হ্যাঁ", "জি", "হুম", "ঠিক আছে", "হ্যা", "অবশ্যই" | "Yes", "Yeah", "Sure", "Okay" |
| ❌ No / Cancel | "না", "চাই না", "বাতিল", "আর দরকার নেই" | "No", "Cancel", "Not needed" |
| 🤔 Unclear / Ambiguous | "দেখি", "পরে বলব", "এখন না", "একটু ভাবি" | "Maybe", "Later", "Not now" |

---

### 4. Agent Response Based on Intent

- **If Confirmed:**  
  **Agent:** ধন্যবাদ! আপনার অর্ডারটি কনফার্ম করা হয়েছে। খুব শিগগিরই ডেলিভারি পাঠানো হবে।  
  *(Thank you! Your order has been confirmed. Delivery will be sent soon.)*

- **If Not Confirmed:**  
  **Agent:** ঠিক আছে, আপনার অর্ডারটি বাতিল করা হলো। ধন্যবাদ সময় দেওয়ার জন্য।  
  *(Okay, your order has been canceled. Thank you for your time.)*

- **If Unclear:**  
  **Agent:** বুঝতে পারিনি, আপনি কি অর্ডারটি কনফার্ম করতে চান?  
  *(I didn’t catch that. Would you like to confirm the order?)*

---

### 5. Closing
**Agent (Bangla):** ধন্যবাদ, শুভ দিন!  
**Agent (English):** Thank you, have a great day!
