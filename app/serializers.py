from rest_framework import serializers
from app.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone")

    def to_internal_value(self, data):
        data['user'] = self.context.get('user')
        return data

    def to_representation(self, instance):
        return {
            "name": instance.name,
            "email": instance.email,
            "phone": instance.phone
        }
