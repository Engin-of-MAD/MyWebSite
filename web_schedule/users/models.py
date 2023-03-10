from django.contrib.auth.models import User
from django.db import models


class TypesOrgs(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        db_table = 'types_orgs'

    orgs = models.CharField(max_length=32)
    orgs_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.orgs


class Profile(models.Model):
    bio = models.TextField(null=True, blank=True, verbose_name="ФИО")
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    tg = models.CharField(max_length=50, null=True, blank=True, verbose_name="Телеграм")
    type_org = models.ForeignKey(TypesOrgs, on_delete=models.PROTECT, blank=True, verbose_name="Типы организаций")
    slag = models.SlugField(unique=True, blank=True)

    class Meta:
        db_table = 'users_profiles'

    def __str__(self):
        return str(self.user)
