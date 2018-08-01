from django.db import models

# Create your models here.
class Model(models.Model):
    field = models.IntegerField()

    def to_dict(self):
        return { 'pk': self.pk, 'field': self.field }
