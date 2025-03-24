from django.db import models
import uuid
from user.models import Profile, Location


# Create your models here.
class posts(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200, null=False)
    subtitle =models.CharField(max_length=200)
    content = models.CharField(max_length=2000,null=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.author.user} post'