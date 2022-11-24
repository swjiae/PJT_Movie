from rest_framework.response import Response
# method Decorator
from rest_framework.decorators import api_view
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# 응답 상태 표시하기
from rest_framework import status
# DB 값 불러오기
from django.shortcuts import get_object_or_404, get_list_or_404
# model, serializer 불러오기
from .models import Movie, Credit, Review, Comment, Trailer
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer, CreditSerializer, TrailerSerializer
from django.http import JsonResponse

# Create your views here.


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies2 = movies[:10]
        serializer = MovieListSerializer(movies2, many=True)
        return Response(serializer.data)

# Create your views here.


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        nemo = []
        for movie in movies:
            if movie.movie_id == 12:
                nemo.append(movie.genres.all()[0])
        # print(nemo)
        movies2 = []
        for i in range(len(movies)):
            for j in range(len(movies[i].genres.all())):
                if movies[i].genres.all()[j] == nemo[0]:
                    movies2.append(movies[i])
        # movies2 = movies[:10]
        serializer = MovieListSerializer(movies2, many=True)
        return Response(serializer.data)


@ api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@ api_view(['GET'])
def movie_credits(request, movie_pk):
    credits = Credit.objects.filter(movie_id=movie_pk)
    if request.method == 'GET':
        serializer = CreditSerializer(credits, many=True)
        return Response(serializer.data)


@ api_view(['GET'])
def movie_trailer(request, movie_pk):
    trailer = get_object_or_404(Trailer, movie_id=movie_pk)
    if request.method == 'GET':
        serializer = TrailerSerializer(trailer)
        return Response(serializer.data)


@ api_view(['POST'])
# @permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@ api_view(['GET'])
# @permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@ api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@ api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@ api_view(['GET'])
# @permission_classes([IsAuthenticated])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@ api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@ api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        cntLike = movie.like_users.all().count()
        if request.user in movie.like_users.all():
            return JsonResponse({'isLiked': True, 'cntLike': cntLike})
        return JsonResponse({'isLiked': False, 'cntLike': cntLike})
    elif request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user.pk)
            cntLike = movie.like_users.all().count()
            return JsonResponse({'isLiked': False, 'cntLike': cntLike})
        else:
            movie.like_users.add(request.user)
            cntLike = movie.like_users.all().count()
            return JsonResponse({'isLiked': True, 'cntLike': cntLike})


@ api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def review_likes(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        cntLike = review.like_users.all().count()
        if request.user in review.like_users.all():
            return JsonResponse({'isLiked': True, 'cntLike': cntLike})
        return JsonResponse({'isLiked': False, 'cntLike': cntLike})
    elif request.method == 'POST':
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user.pk)
            cntLike = review.like_users.all().count()
            return JsonResponse({'isLiked': False, 'cntLike': cntLike})
        else:
            review.like_users.add(request.user)
            cntLike = review.like_users.all().count()
            return JsonResponse({'isLiked': True, 'cntLike': cntLike})
