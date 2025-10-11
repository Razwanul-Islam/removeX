from django.urls import path
from .views import HomeView, SendContactUsInfoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact-us/submit', SendContactUsInfoView.as_view(), name='send_contact_us_info'),  # New URL pattern    
]