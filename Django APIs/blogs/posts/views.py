from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListApiView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.get_queryset()
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content')
        }
        
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  PostDetailView(APIView):
    
    def get_post(self, post_title):
        try:
            post = Post.objects.get(title = post_title)
        except Post.DoesNotExist:
            return None
        
        return post
    
    def get(self, request, post_title):
        post = self.get_post(post_title)
        
        if not post:
            return Response(
                {"res": "No post exists with this title"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = PostSerializer(post)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, post_title):
        post = self.get_post(post_title)
        
        if not post:
            data = {
                'title': request.data.get('title'),
                'content': request.data.get('content')
            }
            serializer = PostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # print(request.data)
        # if request.data.get('title', None):
        #     post.title = request.data.get('title')
        
        # if request.data.get('content', None):
        #     post.content = request.data.get('content')
        
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_202_ACCEPTED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, post_title):
        post = self.get_post(post_title)
        
        if not post:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        post.delete()
        
        return Response(
            {"res": "Object Deleted"}, 
            status=status.HTTP_200_OK
        )