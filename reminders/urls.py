from django.urls import path
from .views import *


   

# UserReminderView
# UserPrescriptionView
#ReminderListView

urlpatterns = [
    path('reminders/', ReminderListView.as_view(), name="allreminders"),
     path('<pk>', ReminderView.as_view(), name="reminder"),
    path('prescriptions/', PrescriptionView.as_view(), name="allprescriptions"),
    path('reminders/<str:pk>/', UserReminderView.as_view(), name="userreminders"),
    # path('prescriptions/<pk>/', UserPrescriptionView.as_view(), name="userprescriptions"),
]
