from django.db import models
from users.models import User
from django.conf import settings
from django.core.exceptions import ValidationError

class ContestPostAdmin(models.Model):
    category = models.CharField(max_length=100)
    poster = models.TextField()
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'admin'},
        related_name='contest_posts'
    )
    text_field = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        super().clean()
        if self.admin and self.admin.role != 'admin':
            raise ValidationError("The selected user is not an admin.")

class ContestUser(models.Model):
    POSITION_CHOICES = [(0, 'None'), (1, 'First'), (2, 'Second'), (3, 'Third')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.TextField()
    position = models.IntegerField(choices=POSITION_CHOICES, default=0)
