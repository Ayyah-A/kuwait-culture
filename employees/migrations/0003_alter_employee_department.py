# Generated by Django 4.2.7 on 2023-12-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('cultural counselor’s office', 'Cultural Counselor’s Office'), ('cultural attache’s office', 'Cultural Attache’s Office'), ('accounting', 'Accounting'), ('administration', 'Administration'), ('authentication', 'Authentication'), ('graduate', 'Graduate'), ('undergraduate', 'Undergraduate'), ('translation', 'Translation'), ('information technology', 'Information Technology')], max_length=200),
        ),
    ]
