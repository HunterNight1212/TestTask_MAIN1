from django.db import models


# поля для работы приложения

# поле подкатегория
class Subcategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# поле категория
class Category(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name


# поле статус
class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# поле тип
class Tipe(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# поле для записей объединяющее все поля
class DataDDS(models.Model):
    date_create = models.DateTimeField(auto_now_add=True, editable=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    tipe = models.ForeignKey(Tipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    summ = models.FloatField(default=0.0)
    comment = models.TextField(blank=True, null=True)
