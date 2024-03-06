from django.db import models

# Create your models here.



class Produkt(models.Model):
    produktname  = models.CharField("Наименование",max_length=100,blank=True,null=True)
    size= models.IntegerField("Размер")  
    color=models.CharField("Цвет", max_length=100)
    price=models.FloatField("Цена", max_length=100)  
    
     
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        #ordering = ['prodaja']
         
    
    def __str__(self) -> str:
        return self.color

