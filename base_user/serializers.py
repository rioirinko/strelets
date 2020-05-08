from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'gender', 'birthday', 'country', 'passport', 'password',
                  'token', )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    # def is_valid(self, raise_exception=False):
    #     is_valid = super().is_valid(raise_exception=True)
    #
    #     if self.validated_data['password'] != self.validated_data['password_repeat']:
    #         raise serializers.ValidationError(detail='Ваши пароли не совпадают')
    #
    #     return is_valid


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Для входа требуется адрес электронной почты.'
            )

        if password is None:
            raise serializers.ValidationError(
                'Для входа требуется пароль.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Пользователь с этим адресом электронной почты и паролем не найден.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'Этот пользователь был деактивирован.'
            )

        return {
            'token': user.token,
        }
