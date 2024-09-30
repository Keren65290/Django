from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),  # Adjust this based on your existing migrations
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_description',
            field=models.TextField(null=True),  # You can change null=True based on your needs
        ),
    ]