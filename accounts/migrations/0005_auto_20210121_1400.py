# Generated by Django 3.1.5 on 2021-01-21 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20210120_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilelinks',
            options={'verbose_name': 'Profile Links', 'verbose_name_plural': 'Profile Links'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
