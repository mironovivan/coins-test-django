# Generated by Django 2.0.5 on 2018-05-10 15:36

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', utils.models.DefaultCharField(max_length=255, primary_key=True, serialize=False)),
                ('owner', utils.models.DefaultCharField(max_length=255)),
                ('balance', utils.models.CurrencyField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
    ]
