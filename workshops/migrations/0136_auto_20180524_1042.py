# Generated by Django 2.0.5 on 2018-05-24 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0135_auto_20180519_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['family', 'personal'], 'permissions': [('can_access_restricted_API', 'Can this user access the restricted API endpoints?')]},
        ),
    ]
