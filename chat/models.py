from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=50, unique=True)
    member = models.ManyToManyField(User, blank=True)

    def join(self, user):
        self.member.add(user)
        self.save()
        return

    def leave(self, user):
        self.member.remove(user)

    def __str__(self):
        return self.name
