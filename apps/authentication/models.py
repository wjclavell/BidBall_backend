from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.contrib.postgres.fields import ArrayField  # this allows the use of Arrays as fields
from rest_framework_jwt.settings import api_settings  # this allows us to set the jwt settings

# setting jwt payload
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, first_name=None, last_name=None):
        if username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have a valid email address")

        # here we are creating the user object
        user = self.model(
            username=username,
            email=self.normalize_email(email),  # inherited from BaseUserManager class, sets email to lowercase
            first_name=first_name,
            last_name=last_name,
            is_staff=False
        )

        user.set_password(password)  # encrypts password and stores it in database
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Superusers must have a password")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)  # username & email unique to each user
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)  # name fields can be empty
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)  # default True for testing purposes, can be changed later to False
    created_at = models.DateTimeField(auto_now_add=True)  # creation time is 'frozen' can't be edited
    updated_at = models.DateTimeField(auto_now=True)  # current time, will be changed on update
    # will be used to upload file or image url
    profile_pic = models.TextField(
        default='https://res.cloudinary.com/wjclavell/image/upload/v1600292929/P4/bidball_default-user_lrcu7s.png')
    balance = models.IntegerField(default=100)  # users start with 100 coins when they sign up
    correct = models.IntegerField(default=0)  # used to keep track of user's correct picks
    incorrect = models.IntegerField(default=0)  # used to keep track of user's incorrect picks
    # used to determine what category the app will be defaulted to
    favorite_league = models.CharField(max_length=25, null=True, blank=True)  # corresponds to sport_id in 'the rundown'
    # will be used for user to update
    favorite_teams = ArrayField(models.CharField(max_length=255, blank=True, default=''), default=list, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # We are telling that the UserManager class defined above
    # that it should manage objects of this type
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this(self) user's
        instance and has an expiry date set to 60 days into the future
        """
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        return token
