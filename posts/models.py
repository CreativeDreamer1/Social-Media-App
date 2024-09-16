from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.created_at