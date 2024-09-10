from rest_framework import serializers
from .models import Blog
from .firestore import upload_image_to_firebase_storage

class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(), source='get_tags_list', write_only=True)
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'image', 'tags', 'image_url', 'is_featured_story', 'created_at']

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        tags = validated_data.pop('get_tags_list')
        validated_data['tags'] = ','.join(tags)

        if image:
            validated_data['image_url'] = upload_image_to_firebase_storage(image)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        tags = validated_data.pop('get_tags_list', None)

        if tags:
            validated_data['tags'] = ','.join(tags)

        if image:
            validated_data['image_url'] = upload_image_to_firebase_storage(image)

        return super().update(instance, validated_data)
