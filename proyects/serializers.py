from rest_framework import serializers
from .models import Proyect


class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'technology', 'link', 'created', 'updated')
        read_only_fields = ('created', 'updated')
