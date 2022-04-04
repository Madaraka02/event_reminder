from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import permissions
from .models import *
from .serializers import *


class ReminderListView(ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = (permissions.AllowAny, )

class ReminderView(RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = (permissions.AllowAny, )

class PrescriptionView(RetrieveAPIView):    
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = (permissions.AllowAny, )


class UserReminderView(RetrieveAPIView):
    serializer_class = ReminderSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        current_user_reminder = Reminder.objects.all()
        return current_user_reminder

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        user_reminders =   Reminder.objects.filter(user=params['pk']) 
        #user_reminders =   Reminder.objects.filter(user=request.user)   
        serializer = ReminderSerializer(user_reminders, many=True)
        return Response(serializer.data)

# class UserPrescriptionView(RetrieveAPIView):    
#     queryset = Prescription.objects.filter(user=request.user)
#     serializer_class = PrescriptionSerializer

#     def get_queryset(self):
#             return Reminder.objects.all().filter(user=self.request.user)