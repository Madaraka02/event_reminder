from django.urls import path
from .views import *


   

# UserReminderView
# UserPrescriptionView
#ReminderListView

urlpatterns = [
    #show all reminders and form for creating new reminders
    path('reminders/', ReminderListView.as_view(), name="allreminders"),
    #show reminders for the current logged in user
    path('user/reminders/', UserReminderView.as_view(), name="ureminders"),
    #retrieve reminder by id
    path('reminders/<pk>/', ReminderView.as_view(), name="reminder"),
    #show all prescriptions and allow create
    path('prescriptions/', PrescriptionListView.as_view(), name="allprescriptions"),
    #retrieve prescription by id
    path('prescriptions/<pk>/', PrescriptionView.as_view(), name="allprescriptions"),
    #retrieve all medicines
    path('medicines/', MedicineListView.as_view(), name="medicines"),
    # path('reminders/<str:pk>/', UserReminderView.as_view(), name="userreminders"),
    # path('prescriptions/<pk>/', UserPrescriptionView.as_view(), name="userprescriptions"),
]
