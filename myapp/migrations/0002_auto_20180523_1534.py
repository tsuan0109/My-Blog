# Generated by Django 2.0.4 on 2018-05-23 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='postblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pbtitle', models.CharField(max_length=100)),
                ('pbtime', models.DateTimeField(auto_now_add=True)),
                ('pbcontent', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='ptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
