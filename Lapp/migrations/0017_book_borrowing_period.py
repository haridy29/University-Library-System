# Generated by Django 3.2.5 on 2021-07-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lapp', '0016_remove_book_borrowing_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Borrowing_period',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]
