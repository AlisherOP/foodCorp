from rest_framework import serializers
from .models import Item

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields= ('id', 'user_name', 'item_name',
                'item_desc', 'item_price','item_cal', 'item_image')
