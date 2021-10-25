from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from users.UserSerializers import ReadSerializer, WriteUserSerializer
from rest_framework.permissions import IsAuthenticated
from posts.PostSerializers import PostSerializer


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        return Response(ReadSerializer(request.user).data)

    def put(self, request):
        serializer = WriteUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(ReadSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class BookmarksView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PostSerializer(user.favs.all(), many=True).data
        return Response(serializer)

    def put(self, request):
        pass