# Generated by Django 3.2.5 on 2021-07-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lapp', '0013_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
