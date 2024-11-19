from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateField(auto_now=True, verbose_name="Update date")

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} sent message: {self.subject}"

