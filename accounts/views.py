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
        phone = data['phone']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(phone=phone).exists():
                return Response({'error': 'phone number already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'password must be atleast 6 characters'})

                else:
                    user = User.objects.create_user(phone=phone, password=password, name=name)

                    user.save()    
                    return Response({'success': 'User created successfully'})


        else:
            return Response({'error': 'passwords do not match'})
