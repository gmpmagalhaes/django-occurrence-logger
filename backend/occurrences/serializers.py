from rest_framework import serializers
from .models import Occurrence

class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = '__all__'
        read_only_fields = ('user','state',)

class UpdateOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ['state']
        read_only_fields = ('description','location','category','created_at','modified_at','user')