# Generated by Django 4.1.1 on 2022-09-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_rename_catergory_name_category_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cart_image',
            field=models.ImageField(blank=True, upload_to='categories/photos/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]