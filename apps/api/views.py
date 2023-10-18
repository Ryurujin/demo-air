from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import *
from apps.post.models import *


#post
class Post_views_list(APIView):
    
    def get(self, request):
        posts = ModelsPost.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)  

    def post(self, request):
        serializer = PostSerializers(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Post_views_detail(APIView):   

    def get(self, request, pk):
        post = ModelsPost.objects.get(pk=pk)
        serializer = PostSerializers(post)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        post = ModelsPost.objects.get(pk=pk)
        serializer = PostSerializers(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = ModelsPost.objects.get(pk=pk)
        post.delete
        return Response('Deleted', status=HTTP_204_NO_CONTENT)
    


