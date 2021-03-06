from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Ticket(models.Model):
    """
    The model for a ticket
    """
    STATUS_CHOICES = (
        ('TO DO', 'To Do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done')
    )

    TICKET_CHOICES = (
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature')
    )

    author = models.ForeignKey(User, null=True,)
    title = models.CharField(max_length=255)
    description = models.TextField()
    ticket_type = models.CharField(max_length=20, choices=TICKET_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO DO')
    upvotes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    most_recent_update = models.DateTimeField(blank=True, null=True,
    default=timezone.now)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title

class TicketComment(models.Model):
    """
    The model for a comment
    """
    comment = models.TextField()
    ticket = models.ForeignKey(Ticket)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   

    def __str__(self):
        return self.comment 