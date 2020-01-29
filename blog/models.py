from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    #photo = models.ImageField(upload_to='static/background/', default="")
    pub_date = models.DateTimeField('Date published')


    def __str__(self):
        return self.title
