from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer

class ContactFormAPI(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Contact form submitted successfully!"},
                status=status.HTTP_201_CREATED
            )
        return Response({'error': "Invalid inputs"}, status=status.HTTP_400_BAD_REQUEST)
