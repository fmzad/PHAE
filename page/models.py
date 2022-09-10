from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Page(MPTTModel):
    def __str__(self):
        return self.title
    
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
    )
    current_revision = models.ForeignKey(
        'Revision',
        on_delete=models.CASCADE,
        null=False,
        related_name="jin",
    )

# Create your models here.
class Revision(models.Model):
    revision_number = models.IntegerField()
    # revision_page = models.ForeignKey(
    #     Page,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )
    content = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )
    page = models.ForeignKey(
    	Page,
        on_delete=models.CASCADE,
        null=True,
    )
    # user
    # datetime
    # type