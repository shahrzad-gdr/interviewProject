from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg

from blog.models import Post


class Rate(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rank = models.SmallIntegerField(blank=True, null=True)  # rank can be 0, 1, 2, 3, 4, 5

    @staticmethod
    def average(post_id):   # average of all ranks for each post
        average_rank = Rate.objects.filter(post_id=post_id).aggregate(Avg('rank'))
        return average_rank['rank__avg'] or 0

    @staticmethod
    def count(post_id):    # count of ranks for each post
        count = Rate.objects.filter(post_id=post_id).count()
        return count or 0


    def __str__(self):
        return f"{self.user} , {self.post}"

