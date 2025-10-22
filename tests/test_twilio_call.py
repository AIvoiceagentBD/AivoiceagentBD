import os
from twilio.rest import Client

# --- ACCOUNT CREDENTIALS (CONFIRM THESE ARE CORRECT) ---
# Replace these strings with your actual values.
# Your Account SID from twilio.com/console
account_sid = "------------------------------" 
# Your Auth Token from twilio.com/console
auth_token = "------------------------------"

# Initialize the Twilio Client
client = Client(account_sid, auth_token)

# --- Define the call parameters (CONFIRM THESE ARE CORRECT) ---

# The Twilio Phone Number you purchased (must be in E.164 format: +1234567890)
twilio_number = "-----------------"  

# The phone number to call (must be in E.164 format: +1234567890)
to_number = "--------------------"      

# The URL of the TwiML document Twilio will fetch when the call is answered.
# This TwiML URL is where your voice instructions are hosted.
twiml_url = "https://handler.twilio.com/-------------------------"

print(f"Attempting to call {to_number} from {twilio_number}...")

try:
    # Make the actual call request
    call = client.calls.create(
                                to=to_number,
                                from_=twilio_number,
                                url=twiml_url
                            )

    # Print the Call SID (a unique identifier for the call)
    print(f"Call initiated successfully! SID: {call.sid}")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Possible reasons for failure:")
    print("1. Authentication: Account SID or Auth Token is incorrect.")
    print("2. Phone Number Format: Numbers are not in E.164 format (e.g., must start with +880 or +1).")
    print("3. GeoPermissions: Your Twilio number may not be allowed to call Bangladesh (country code 880). Check your Twilio Voice Geo-Permissions.")
