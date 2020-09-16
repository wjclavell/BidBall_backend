from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
# not all the models need CRUD, sometimes all we need to do is read only
from rest_framework.viewsets import ReadOnlyModelViewSet
# we can allow all the users to see this view
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User


# Create your views here.
class RegistrationAPIView(APIView):
    # allow any user to hit this endpoint
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "email": request.data.get('email'),
                "password": request.data.get('password'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name'),
            }

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password'),
            }

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# TODO Create delete route to DELETE a user and UPDATE route to change username & favorites
class SingleUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserListSerializer

    model = User

    def get_object(self, queryset=None):
        return self.request.user

    # def get_queryset(self):
    #     # localhost:api/8000/auth/users/pk/
    #     user = User.objects.get(id=self.kwargs["pk"])
    #     return user
