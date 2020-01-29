from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + '번 / ' + self.name

# class Shop(models,Model):
#     ID = models.CharField(max_length=255)
#     TITLE = models.CharField(max_length=255)
#     CONTENT = models.CharField(max_length=255)
#     WRITER = models.CharField(max_length=255)
#     HIT = models.CharField(max_length=255)
#     C_DATE = models.CharField(max_length=255)

#     def __str__(self):
#         return self.ID,self.TITLE,self.CONTENT

