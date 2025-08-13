from rest_framework.serializers import ModelSerializer
from .models import ContactUsModel


class ContactSerializer(ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = ["id","name","email","contactno","address","dob","gender"]