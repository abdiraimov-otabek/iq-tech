import os
import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        BOT_TOKEN = os.getenv("BOT_TOKEN")
        CHAT_ID = os.getenv("CHAT_ID")

        if not BOT_TOKEN or not CHAT_ID:
            print("⚠️ BOT_TOKEN yoki CHAT_ID topilmadi!")
            return

        message = (
            f"📩 Yangi ariza keldi!\n\n"
            f"👤 Ism: {contact.name}\n"
            f"📞 Telefon: {contact.phone_number}\n"
            f"📝 Habar: {contact.request}"
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}

        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()  # HTTP xatolarni ko‘rsatadi
        except requests.exceptions.HTTPError as http_err:
            print(f"Telegram HTTP xato: {http_err} - {response.text}")
        except requests.exceptions.RequestException as err:
            print(f"Telegram so‘rov xato: {err}")
