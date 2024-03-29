from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, db_index=True) #indexation(db_index)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers', blank=True)

    class Meta:
        indexes=[
            models.Index(fields=["id"], name="id_index")
        ]
        permissions = [
            ('special_status', 'Can read all books')
        ]

    def __str__(self):
        return self.title

    # Fonction à utiliser pour l'url de detail dans le template html
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class Review(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review

