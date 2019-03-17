from django.http import JsonResponse
from . import models
from . import serializers
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def api_post(request):
    if request.method == 'GET':
        posts = models.Post.objects.all()
        serialaizer = serializers.PostSerializer(posts, many=True)
        return Response(serialaizer.data)


@api_view(['POST'])
def add_post(request):
    if request.method == 'POST':
        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_REQUEST)
# class PostViewSet(viewsets.ModelViewSet):
#     """ViewSet for the Post class"""

    # queryset = models.Post.objects.all()
    # serializer_class = serializers.PostSerializer
    # # permission_classes = [permissions.IsAuthenticate]
    # permission_classes = [permissions.AllowAny]
    # def list(self, request):
    #     pass
    #
    #
    # def create(self, request):
    #     pass
