# Generated by Django 4.0.3 on 2022-03-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_book_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AddField(
            model_name='users',
            name='books',
            field=models.ManyToManyField(to='book.book'),
        ),
    ]