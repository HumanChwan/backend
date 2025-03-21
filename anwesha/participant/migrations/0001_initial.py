# Generated by Django 4.1 on 2022-10-06 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('user', '0008_alter_user_accomadation_selected_alter_user_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anwesha_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.events')),
                ('team_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.participant')),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('paid', 'paid'), ('unpaid', 'unpaid'), ('pending', 'pending')], default='unpaid', max_length=10)),
                ('reference_id', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('payer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participant.participant')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.events')),
                ('Team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
