from django.urls import path
from .views import *


   

# UserReminderView
# UserPrescriptionView

urlpatterns = [
    path('reminders/', ReminderView.as_view(), name="allreminders"),
    path('prescriptions/', PrescriptionView.as_view(), name="allprescriptions"),
    path('reminders/<pk>/', UserReminderView.as_view(), name="userreminders"),
    # path('prescriptions/<pk>/', UserPrescriptionView.as_view(), name="userprescriptions"),
]
