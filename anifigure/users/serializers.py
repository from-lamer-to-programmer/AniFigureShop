from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password",)
        extra_kwargs = {
        "password": {"write_only": True},
        "email": {"required": False},
        "username": {"required": False},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=False)
    username = serializers.CharField(max_length=255, required=False)
    token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        extra_kwargs = {
            "email": {"required": False},
            "username": {"required": False},
            "password": {"write_only": True, "required": False},
        }
        fields = UserSerializer.Meta.fields + ('token',)
