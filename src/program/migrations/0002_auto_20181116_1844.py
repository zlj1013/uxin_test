# Generated by Django 2.2 on 2018-11-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='remark',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='program',
            name='tester_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='测试人力'),
        ),
    ]
