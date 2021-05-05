# Generated by Django 2.1.5 on 2019-05-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_interview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='apply_method',
            field=models.CharField(choices=[('CO_STAFF', 'CO_STAFF'), ('CO_SITE', 'CO_SITE'), ('JOB_SITE', 'JOB_SITE'), ('EMAIL', 'EMAIL'), ('FRIEND', 'FRIEND'), ('LINKEDIN', 'LINKEDIN'), ('FESTIVAL', 'FESTIVAL'), ('EVENT', 'EVENT'), ('OTHER', 'OTHER')], max_length=10),
        ),
        migrations.AlterField(
            model_name='interview',
            name='response_time_after_review',
            field=models.CharField(choices=[('1WEEK', '1WEEK'), ('2WEEK', '2WEEK'), ('1MONTH', '1MONTH'), ('MORE', 'MORE')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='response_time_before_review',
            field=models.CharField(choices=[('1WEEK', '1WEEK'), ('2WEEK', '2WEEK'), ('1MONTH', '1MONTH'), ('MORE', 'MORE')], max_length=8),
        ),
    ]
