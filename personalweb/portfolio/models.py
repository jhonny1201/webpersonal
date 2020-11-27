from django.db import models
from django.conf import settings

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
