from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.text} - is complete: {self.is_done}"