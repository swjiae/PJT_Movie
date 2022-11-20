from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404

from django.shortcuts import render
from .models import Movie

from .serializers import MovieSerializer

# Create your views here.

@api_view(['GET'])
def main_movielist(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
