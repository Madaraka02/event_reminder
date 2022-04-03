from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions



class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        phone_number = data['phone_number']
        password = data['password']
        password1 = data['password1']

        if password == password1:
            if User.objects.filter(phone_number=phone_number).exists():
                return Response({'error': 'phone number already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'password must be atleast 6 characters'})

                else:
                    user = User.objects.create_user(phone_number=phone_number, password=password, name=name)

                    user.save()    
                    return Response({'success': 'User created successfully'})


        else:
            return Response({'error': 'passwords do not match'})
