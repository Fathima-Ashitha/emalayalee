from django.db import models
from users.models import User

class ContestPostAdmin(models.Model):
    category = models.CharField(max_length=100)
    poster = models.TextField()
    admin = models.ForeignKey('admins.Admin', on_delete=models.CASCADE)
    text_field = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()

class ContestUser(models.Model):
    POSITION_CHOICES = [(0, 'None'), (1, 'First'), (2, 'Second'), (3, 'Third')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.TextField()
    position = models.IntegerField(choices=POSITION_CHOICES, default=0)
