# Generated by Django 3.2.5 on 2021-07-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lapp', '0007_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
