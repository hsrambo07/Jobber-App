from rest_framework.response import Response
from .models import User
from rest_framework.decorators import api_view
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.models import TokenModel
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.views import LoginView
from rest_framework import status
from django.conf import settings


class CustomLoginView(LoginView):
    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }
            serializer = serializer_class(
                instance=data, context=self.get_serializer_context()
            )
        else:
            serializer = serializer_class(
                instance=self.token, context=self.get_serializer_context()
            )

        if self.user.username == '':
            check = {'username_exists': False}
        else:
            check = {'username_exists': True}
        response = Response({**serializer.data, **check}, status=status.HTTP_200_OK)
        return response


class CustomSocialLoginView(CustomLoginView):
    serializer_class = SocialLoginSerializer


class GoogleLogin(CustomSocialLoginView):
    permission_classes = ()
    adapter_class = GoogleOAuth2Adapter
    token_model = TokenModel
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        url = self.request.data.get('callback_url')
        self.callback_url = url
        return super(GoogleLogin, self).post(request, *args, **kwargs)
