from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Rate
from account.serializers import PostSerializer
from blog.models import Post


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            docs for swagger:
                * authenticated user
                * return all posts

        """
        user = self.request.user  # Get the authenticated user
        posts = Post.objects.all()
        user_id = user.id

        # Fetch the ratings for the user
        user_ratings = Rate.objects.filter(user_id=user_id)

        # Create a dictionary of post IDs and their corresponding ratings by the user
        user_ratings_dict = {rating.post_id: rating.rank for rating in user_ratings}

        # Loop through posts and add user's rank or 'None' if not rated
        for post in posts:
            post.rank = user_ratings_dict.get(post.id, None)

        return posts
