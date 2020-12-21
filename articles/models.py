from django.db import models

# will output corresponding front-end widgets depending on what fields are entered in the model
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField
    body = models.TextField
    date = models.DateTimeField(auto_now_add=True)
