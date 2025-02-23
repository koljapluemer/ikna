from django.db import models
from django.conf import settings


class Word(models.Model):
    native = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    script = models.CharField(max_length=100, blank=True)
    native_info = models.TextField(blank=True)
    translation_info = models.TextField(blank=True)


class WordPractice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vocab_practices")
    word = models.ForeignKey('Word', on_delete=models.CASCADE, related_name="vocab_practices")
    
    card_id = models.BigIntegerField(null=True, blank=True)
    state = models.CharField(max_length=20, default="Learning")  # We'll store the name of the state.
    step = models.IntegerField(null=True, blank=True)
    stability = models.FloatField(null=True, blank=True)
    difficulty = models.FloatField(null=True, blank=True)
    due = models.DateTimeField(null=True, blank=True)
    last_review = models.DateTimeField(null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'word')
    
    def __str__(self):
        return f"{self.user} - {self.word} practice"