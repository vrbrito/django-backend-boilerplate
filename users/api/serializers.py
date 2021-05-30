from rest_framework import serializers

from django.contrib.auth.models import User
from users.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
                'first_name': {
                    'required': True,
                    'allow_blank': False
                },
                'last_name': {
                    'required': True,
                    'allow_blank': False
                },
                'password': {
                    'write_only': True,
                    'required': True,
                    'style': {
                        'input_type': 'password'
                    }
                },
                'email': {
                    'required': True,
                    'allow_blank': False,
                }
            }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        account = Account.objects.create(user=user)
        return user

    
class AccountSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Account
        fields = ['id', 'user', 'preferences', 'data']