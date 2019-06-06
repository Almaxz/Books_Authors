# Generated by Django 2.2 on 2019-04-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bna_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='Authors', to='bna_app.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]