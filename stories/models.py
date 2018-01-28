from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Story(models.Model):
    story_id = models.AutoField(primary_key=True)
    story_title = models.CharField(max_length=500)
    story_content = models.TextField()
    story_created = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('stories:detail_form', kwargs={'pk': self.pk})

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating_value = models.IntegerField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('stories:rating')