from django.db import models

# Create your models here.
class Promotion(models.Model):
    decription=models.CharField(max_length=255)
    dicount=models.FloatField()


class Collection(models.Model):
    title=models.CharField(max_length=255)
    featured_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')

class Product(models.Model):
    title=models.CharField(max_length=299)
    discription= models.TextField()
    slug=models.SlugField()
    unit_price=models.DecimalField(max_digits=5,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotion=models.ManyToManyField(Promotion)

class Customer(models.Model):
    membership_bronze='B'
    membership_gold='G'
    membership_silver='S'
    Membership_choice=[
        ( membership_bronze,'Bronze'),
         ( membership_gold,'Gold'),
          ( membership_silver,'Silver')
    ]
    
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=11)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=Membership_choice,default=membership_bronze)

class Order(models.Model):
    
    pending_statue='B'
    Comblete_statue='G'
    faild_statue='S'
    payment_status=[
         (pending_statue,'Pending'),
         (Comblete_statue ,'Comblete'),
         (faild_statue,'Faild')
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_statue=models.CharField(max_length=1,choices=payment_status,default=pending_statue)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

class Ordered_item(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=5,decimal_places=2)



class Adress(models.Model):   
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    cutomer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()   



       

    

