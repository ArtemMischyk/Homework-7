from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="An author's full name. (Example: W. Shakespear or Mihail Afanasievich Bulgakov)", max_length=100)),
                ('date_of_birth', models.DateField(help_text="A date of author's birth (or Null, if unknown).", null=True)),
                ('date_of_death', models.DateField(help_text="A date of author's death (or Null, if alive or unknown).", null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A book genre. (example: Science Fiction)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=100)),
                ('year', models.SmallIntegerField()),
                ('status', models.CharField(choices=[('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', max_length=1)),
                ('due_back', models.DateField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='catalog.Genre'),
        ),
    ]