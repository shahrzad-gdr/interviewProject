from rest_framework import serializers

from account.models import Rate
from blog.models import Post



class PostSerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField(read_only=True)

    average_rank = serializers.SerializerMethodField()
    count_rank = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('title', 'rank', 'count_rank', 'average_rank')

    def get_average_rank(self, obj):
        return Rate.average(obj.id)

    def get_count_rank(self, obj):
        return Rate.count(obj.id)


    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['rank'] is None:
            data['rank'] = 'None'
        return data



class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('user', 'post', 'rank')