# Generated by Django 5.0.4 on 2024-04-23 17:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=5, max_digits=7)),
                ('isInStock', models.BooleanField(default=True)),
                ('stock', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Bidon', 'Bidon'), ('Balai', 'Balai'), ('Raclette', 'Raclette'), ('Chiffon', 'Chiffon')], max_length=50)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('totalReviewCount', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('brandName', models.CharField(max_length=100)),
                ('imageUrl', models.URLField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
