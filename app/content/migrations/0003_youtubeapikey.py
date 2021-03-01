# Generated by Django 2.2.12 on 2021-03-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210228_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeAPIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.TextField(db_index=True)),
                ('status', models.CharField(db_index=True, default='active', max_length=50)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
