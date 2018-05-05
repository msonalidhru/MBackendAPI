from rest_framework import serializers

# Serializer Class
class miroSerializer(serializers.Serializer):
    strMiroID = serializers.UUIDField()