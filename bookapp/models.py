from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=60)
    author=models.CharField(max_length=60)
    genre=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField()

    def __str__(self):
        return f'Title : {self.title}, Author: {self.author}, Genre : {self.genre}, Price : {self.price}, Stock : {self.stock} '


class Reader(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
class BookAssignment(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.reader} → {self.book.title}"
