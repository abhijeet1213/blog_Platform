
# Create your models here.
# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
#
#     class Meta:
#         db_table = 'user'
#
#     def __str__(self):
#         return self.username


from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Add related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_service_user_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_service_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )
