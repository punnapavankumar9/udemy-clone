from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    professional_headline = models.CharField(max_length=30,verbose_name="heading", blank=True, null=True, default=None)
    professional_info = models.TextField(max_length=200,validators=[MinLengthValidator(100)], blank=True, null=True)

    def __str__(self):
        return self.user.username


class ProfileLinks(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    website = models.URLField(verbose_name="website url", blank=True, null=True)
    facebook = models.CharField(max_length=50, verbose_name="facebook url", blank=True, null=True)
    twitter = models.CharField(max_length=50, verbose_name="twitter url", blank=True, null=True)
    github = models.CharField(max_length=50, verbose_name="github url", blank=True, null=True)
    linkedin = models.CharField(max_length=50, verbose_name="linkedin url", blank=True, null=True)

    def __str__(self):
        return self.user_profile.user.username

    class Meta:
        verbose_name = "Profile Links"
        verbose_name_plural = "Profile Links"