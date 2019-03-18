from django.http import JsonResponse
from . import models
from . import serializers
from rest_framework import viewsets, permissions, status
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
            return Response(serializer.errors, status=status.HTTP_400_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_post_detail(request, pk):
    post = models.Post.objects.get(pk=pk)
    if request.method == 'GET':
        serialaizer = serializers.PostSerializer(post)
        return Response(serialaizer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serialaizer = serializers.PostSerializer(post, data=request.data)
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data)
        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return REsponse(status=status.HTTP_204_NO_CONTENT)
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
