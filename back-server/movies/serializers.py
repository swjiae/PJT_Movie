from rest_framework import serializers
from .models import Movie, Genre, Credit, Review, Comment, Trailer
from django.contrib.auth import get_user_model

# movie list
class MovieListSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

# review list
class ReviewListSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__' 
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user')


# comment list
class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user')


# review detail
class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)


# movie detail
class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)   
    genres = GenreSerializer(many=True, read_only=True)
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'  
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class CreditSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Credit
        fields = '__all__'


class TrailerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trailer
        fields = '__all__'