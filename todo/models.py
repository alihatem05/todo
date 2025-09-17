from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
        (4, "Critical")
    ]
    STATUS_CHOICES = [
        ("pending", "Pending.."),
        ("completed", "Completed!")
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    status = models.TextField(choices=STATUS_CHOICES, default="pending")
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title