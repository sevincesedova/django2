from django.db import models

# Create your models here.

class books(models.Model):
    user=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    book=models.CharField(max_length=100)
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username