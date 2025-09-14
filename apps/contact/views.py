import os
import requests
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        BOT_TOKEN = os.getenv("BOT_TOKEN")
        CHAT_ID = os.getenv("CHAT_ID")

        message = (
            f"📩 Yangi ariza keldi!\n\n"
            f"👤 Ism: {contact.name}\n"
            f"📞 Telefon: {contact.phone_number}\n"
            f"📝 Habar: {contact.request}"
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}

        try:
            requests.post(url, data=payload)
        except Exception as e:
            print("Telegramga yuborishda xato:", e)
