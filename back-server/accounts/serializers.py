from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model

class RegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image
    username = None
    nickname = serializers.CharField(max_length=10)
    profile_img = serializers.ImageField(required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['profile_img'] = self.validated_data.get('profile_img', '')
        return data


class LoginSerializer(LoginSerializer):
    username = None


UserModel = get_user_model()
class UserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'profile_img'):
            extra_fields.append('profile_img')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('USERNAME_FIELD', 'nickname', 'profile_img')