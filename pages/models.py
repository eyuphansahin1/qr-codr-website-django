from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True, max_length=50,)
    isActive = models.BooleanField(default=False)
    #imageUrl = models.CharField(max_length = 50 , blank = False )
    image = models.ImageField(upload_to="images",default="")
    def __str__(self) : 
        return f"{self.name} category "
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    isActive = models.BooleanField(default=False)
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE,related_name='products')
    person_type = models.CharField(max_length=20, null=True, blank=True, choices=[('per_person', 'Per Person'), ('total', 'Total')])
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)  # Price field added

    def __str__(self):
        return f"{self.name} product"
