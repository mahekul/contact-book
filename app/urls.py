from django.conf.urls import url
from app import views

contact_details = views.ContactViewset.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^contact-book/?$', contact_details),
]
