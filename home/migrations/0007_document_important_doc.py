# Generated by Django 4.2.7 on 2024-02-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='important_doc',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
