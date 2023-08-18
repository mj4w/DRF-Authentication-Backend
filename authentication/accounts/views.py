from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

@api_view(['POST'])
def create_jwt_token(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Authenticate the user
    user = authenticate(username=email, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
