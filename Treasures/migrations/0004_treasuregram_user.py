# Generated by Django 2.1.1 on 2018-10-27 20:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Treasures', '0003_treasuregram_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasuregram',
            name='User',
            field=models.ForeignKey(default=1, on_delete=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
