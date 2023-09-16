from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Your custom authentication logic goes here.
        # Call the parent class's authenticate method to perform JWT authentication.
        user, validated_token = super().authenticate(request)

        # You can add custom checks or validations here.
        # For example, if you want to deny access to users with a specific condition:
        if user and user.some_condition:
            raise exceptions.AuthenticationFailed('Access denied for this user.')

        return user, validated_token
