import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from app.models import Contact


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page-size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('next', super(Pagination, self).get_next_link()),
            ('previous', super(Pagination, self).get_previous_link()),
            ('results', data)
        ]))


class ContactFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = Contact
        fields = ['name', 'email']
        exclude = []
