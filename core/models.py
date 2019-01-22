from django.db import models


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)


class Entry(BaseModel):
    class Meta:
        verbose_name = 'Blog entry'
        verbose_name_plural = 'Blog entries'
        
    title = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.pk, self.title)

class Comment(BaseModel):
    entry = models.ForeignKey(
        "core.Entry", on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField()

    def __str__(self):
        return "{} - {} - {}".format(
            self.id, self.entry.title, self.comment
        )
