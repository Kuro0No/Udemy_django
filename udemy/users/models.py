from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)

from courses.models import Course
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations =  True
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            return ValueError('Superuser must have is_staff True')

        if other_fields.get('is_superuser') is not True:
            return ValueError('Superuser must have is_superuser True')

        return self.createuser(email, password, name, **other_fields)

    def create_user(self, email, password, name, **other_fields):
        if not email:
            raise ValueError('You must provide a valid email')

        email=self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)
        user.set_password(password)

        user.save()

        return user

class User(AbstractBaseUser,PermissionsMixin):
    name =models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    created= models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    is_staff=models.BooleanField(default=False)
    paid_courses=models.ManyToManyField(Course)

    USERNAME_FIELD = 'email'
    REQUIRE_FIELD =['name']
    objects = UserManager()

    def __str__(self) -> str:
        return self.name + " " + self.email
        
