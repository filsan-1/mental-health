from django.contrib.auth.models import User
from django.db import models

class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=50)  # e.g., Happy, Anxious
    note = models.TextField(blank=True)

class SessionSummary(models.Model):
    provider = models.ForeignKey(User, related_name='provider', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    session_date = models.DateTimeField(auto_now_add=True)
    triggers = models.TextField(blank=True)
    coping_strategies = models.TextField(blank=True)
    progress_notes = models.TextField()

class PrivacySetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allow_data_sharing = models.BooleanField(default=False)
