# Generated by Django 4.0.2 on 2022-02-16 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.period'),
        ),
        migrations.AddField(
            model_name='case',
            name='respondent',
            field=models.ManyToManyField(to='user.Respondent'),
        ),
        migrations.AddField(
            model_name='case',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='case.state'),
        ),
    ]
