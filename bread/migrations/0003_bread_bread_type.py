# Generated by Django 3.1.4 on 2020-12-17 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bread', '0002_bread_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bread',
            name='bread_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
            preserve_default=False,
        ),
    ]