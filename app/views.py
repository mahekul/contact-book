from rest_framework import viewsets, filters
from app.models import Contact
from app.serializers import ContactSerializer
from app.utils import Pagination, ContactFilter
from django_filters import rest_framework as rf_filters


class ContactViewset(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    filter_backends = (rf_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ContactFilter
    pagination_class = Pagination

    def get_serializer_context(self):
        context = super(ContactViewset, self).get_serializer_context()
        context.update({
            "user": self.request.user,
        })
        return context

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def get_object(self):
        return Contact.objects.get(email=self.request.data.get('email'))
