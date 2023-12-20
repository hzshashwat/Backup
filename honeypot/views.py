from django.shortcuts import render
from django.http import HttpResponse
import logging
import requests
import json
import random


logger = logging.getLogger(__name__)
destination_ip = "0.0.0.0"

def main(request):
    # Get the visitor's IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Additional information from the request headers
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    referer = request.META.get('HTTP_REFERER', '')
    accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')

    # Log the information
    logger.info(f"Visitor IP: {ip}, User Agent: {user_agent}, Referer: {referer}, Accept-Language: {accept_language}")


    url = "https://vidyutX.vidyutkavach.live/alert/add_honeypot_alert"

    payload = json.dumps({
    "alert_id": random.randint(0,1000000),
    "type": "Subdomain Scanning",
    "severity": "Medium",
    "attacker_ip": str(ip),
    "destination_ip": destination_ip,
    "port": 80,
    "protocol": "HTTP",
    "action": "on-surviellance",
    "honeypot_id": "H1001",
    "honeypot_name": "Backup Subdomain"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    return render(request, 'honeypot/index.html')