from user_service.models import User
from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user_service.models import User as user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields =  ['email','user_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'error': 'passwords did not match'})

        user = User(email=self.validated_data['email'],
                    user_name=self.validated_data['user_name'],is_active=True)
        user.set_password(self.validated_data['password'])
        user.save()
        return user


