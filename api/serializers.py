# from rest_framework import serializers
# from app.models import Todo


# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=1024, required=False)
#     description = serializers.CharField(required=False)
#     completed = serializers.BooleanField(default=False)

#     def create(self, validated_data):
#         return Todo(id=None, **validated_data)

#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         return instance
