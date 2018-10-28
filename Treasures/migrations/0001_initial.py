# Generated by Django 2.1.1 on 2018-10-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreasureGram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('meterial', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=400)),
            ],
        ),
    ]