from datetime import date
from django.db import models

class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(verbose_name="Data de entrega")
    finished_at = models.DateField()

    class Meta:
        ordering = ["deadline"]

    def mark_has_completed(self):
        self.finished_at = date.today()
        self.save()