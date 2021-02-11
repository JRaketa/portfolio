from django.db import models

class publication(models.Model):
    title = models.CharField(max_length = 300)
    names = models.TextField(max_length = 500)
    year = models.DateField(max_length = 10)
    journal = models.CharField(max_length = 50)



    def __str__(self):
        return self.title

    def year_pretty(self):
        return self.year.strftime('%Y')
