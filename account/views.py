from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Rate
from .serializers import RateSerializer


class RateCreateAPIView(generics.CreateAPIView):
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.request.data.get('post')  # Assuming the post ID is submitted in the request data
        existing_rating = Rate.objects.filter(user=user, post_id=post_id).first()

        if existing_rating:
            serializer.instance = existing_rating
        serializer.save(user=user)
