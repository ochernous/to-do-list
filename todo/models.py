from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ("created", )

    def __str__(self) -> str:
        return self.content
