from django.db.models import *


#post
class ModelsPost(Model):
    name = CharField(
        verbose_name='Name of post',
        max_length=15,
    )
    description = TextField(
        verbose_name='Post description',
        blank=True,
        null=True, 
    )
    def __str__(self):
        return f'{self.name}'
    