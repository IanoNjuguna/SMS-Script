#!/bin/python3

import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '5555555555', # Customise the phone number for your personal use
  'message': 'Hello world', # Customise the message for your personal use
  'key': 'textbelt', # Use key=textbelt to send 1 free text per day
})
print(resp.json())
