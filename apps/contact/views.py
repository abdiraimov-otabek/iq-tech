from rest_framework import generics
from apps.contact.models import Contact
from apps.contact.serializers import ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer