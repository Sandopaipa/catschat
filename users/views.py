from rest_framework import permissions
from .serializers import CreateUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                'message': 'Your profile created'
            }
        )

