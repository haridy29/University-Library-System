# Generated by Django 3.2.5 on 2021-07-15 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lapp', '0015_alter_book_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Borrowing_period',
        ),
    ]
