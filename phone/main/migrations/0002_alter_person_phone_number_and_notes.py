from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('main', '0001_initial')]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
