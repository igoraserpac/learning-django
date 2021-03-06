# Generated by Django 3.2.7 on 2021-09-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_populando_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='publico',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
