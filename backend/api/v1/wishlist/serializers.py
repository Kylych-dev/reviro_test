from rest_framework import serializers
from apps.wishlist.models import WishlistItem

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = [
            # 'id',
            'user',
            'product',
            'created_at'
        ]
