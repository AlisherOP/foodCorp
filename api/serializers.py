from django.contrib.auth.models import User
from rest_framework import serializers
from food.models import Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id", "username", "password"]
        extra_kwargs={"password": {"write_only": True}} # so that the password is not shown to anyone else

    def create(self, validated_data):
        user= User.objects.create_user(**validated_data)
        return user
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields = ["id", "user_name", "item_name",
                "item_desc", "item_cal", "created_at", "author", "item_image", "favourites"]
        extra_kwargs= {"author":{"read_only": True}}
