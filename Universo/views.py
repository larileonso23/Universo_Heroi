from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Universo.serializers import UniversoSerializer, universoLightSerializer

#exemplo de ModelViewSet
class UniversoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Universo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UniversoSerializer

#Separando as Views

class AlunoList(views.APIView):
    def get(self, request):
        alunos = Universo.objects.all()
        serializer = UniversoLightSerializer(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UniversoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlunoDetails(views.APIView):

    def get_object(self, id):
        try:
            return Universo.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id):
        universo = self.get_object(id)
        serializer = UniversoSerializer(universo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        universo = self.get_object(id)
        serializer = universoSerializer(universo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)