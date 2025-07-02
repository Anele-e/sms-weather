from fastapi import FastAPI
import sys
import os

recipient = sys.argv[1] if len(sys.argv) > 1 else exit("Recipient phone ??")
message = sys.argv[2] if len(sys.argv) > 2 else exit("Message ??")
app = FastAPI()

def simulate_sms_sending(recipient, message):
    pass

def simulate_sms_receiving(sender, message):
    pass

