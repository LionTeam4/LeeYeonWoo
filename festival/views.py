from django.http import HttpRequest, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class PostListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request:HttpRequest, format=None):
        posts=Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request:HttpRequest, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def get(self,request:HttpRequest,pk,format=None):
        post=self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request:HttpRequest, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request:HttpRequest, pk, format=None):
        post=self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request:HttpRequest, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InfoListView(APIView):
    def get(self, request:HttpRequest, format=None):
        infos=Info.objects.all()
        serializer = InfoSerializer(infos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request:HttpRequest, format=None):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InfoDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            raise Http404
    def get(self,request:HttpRequest,pk,format=None):
        info=self.get_object(pk)
        serializer = InfoSerializer(info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request:HttpRequest, pk, format=None):
        info = self.get_object(pk)
        serializer = InfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request:HttpRequest, pk, format=None):
        info=self.get_object(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request:HttpRequest, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)