from django.db import models
from online_shop.models import *
from django.contrib.auth.models import User


class Connection(BaseModel):
    """The connection between an admin and user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    admin = models.ForeignKey(
        User, null=True, default=None, on_delete=models.CASCADE, related_name='Admin'
    )

    class Meta:
        verbose_name = 'Connection'
        verbose_name_plural = 'Connections'

    def __str__(self):
        return f'{self.user} and {self.admin}'


class Message(BaseModel):
    sender_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='Sender_user')
    responder_user = models.ForeignKey(
        User, null=True, default=None, on_delete=models.CASCADE, related_name='Responder_user'
    )
    sent_text = models.TextField(blank=False, verbose_name='Sent_text')
    respond_text = models.TextField(blank=False, verbose_name='Respond_text')
    is_responded = models.BooleanField(default=False, verbose_name='Is_responded')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.sent_text}'
