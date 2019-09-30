from rest_framework import serializers

from Universo.models import Universo
from Herois.models import Herois


class ProfessorDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class UnversoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    email = serializers.EmailField()
    prof_favorito = ProfessorDataSerializer()

    def create(self, validated_data):
        professor_data = validated_data.pop('prof_favorito')
        Herois = Herois.objects.get(id=Universo_herois['id'])
        Universo = Universo.objects.create(prof_favorito=Herois, **validated_data)
        return Universo

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        Universo = Herois.objects.get(id=Universo_herois['id'])
        instance.prof_favorito = Universo
        instance.save()
        return instance


class UniversoLightSerializer(serializers.Serializer):
    id = serializers.Integerield()
    nome = serializers.CharField()F
