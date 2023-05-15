from rest_framework import serializers
from .models import Follow
from users.serializers import UserSerializer


class FollowsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "user", "book"]
        depth = 1
