from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class LoginTbl(AbstractUser):
    usertype=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.username
    
class Adopter(models.Model): #User
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password=models.CharField(max_length=100,null=True)
    adopterid=models.ForeignKey(LoginTbl,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

    
class Breeders(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    experience_years = models.IntegerField()
    specialization = models.TextField(help_text="Types of animals bred")
    license_number = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(LoginTbl,on_delete=models.CASCADE)
def __str__(self):
    return self.name

    
# class Shelter_staff(models.Model): #User
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=100)
#     address=models.CharField(max_length=100,null=True)
#     password=models.CharField(max_length=100,null=True)
#     shelterid=models.ForeignKey(LoginTbl,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
 
# class Breeder(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=100)
#     password=models.CharField(max_length=100,null=True)
#     veterinaryid=models.ForeignKey(LoginTbl,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name

# class Trainer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     proof = models.ImageField()
#     phone = models.CharField(max_length=100)
#     password=models.CharField(max_length=100,null=True)
#     trainerid=models.ForeignKey(LoginTbl,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    shopid=models.ForeignKey(LoginTbl,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    quantity = models.IntegerField(null=True)
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=100,null=True)
    shop_id = models.ForeignKey(Shop,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Orders(models.Model):
    owner = models.ForeignKey(Adopter,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.quantity

class Pet(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    VACCIN_CHOICES = [
    (True, 'Yes'),
    (False, 'No'),
]
    HEALTH_CHOICES = [
    ('Good', 'Good'),
    ('Average', 'Average'),
    ('Poor', 'Poor'),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    color = models.CharField(max_length=50,null=True)
    vaccinated = models.BooleanField(default=False,choices=VACCIN_CHOICES)  # True if vaccinated, False otherwise
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True) 
    health_status=models.CharField(max_length=100,null=True,choices=HEALTH_CHOICES) 
    breeder_id = models.ForeignKey(Breeders, on_delete=models.CASCADE, null=True, blank=True)  
    status=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

    
class AdoptionRequest(models.Model):
    EMPLOYMENT_CHOICES = [
        ('Employed', 'Employed'),
        ('Self-employed', 'Self-employed'),
        ('Student', 'Student'),
        ('Unemployed', 'Unemployed'),
    ]

    user = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    living_situation = models.TextField()
    pet_experience = models.TextField()
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES,null=True)
    other_pets_details = models.TextField(blank=True, null=True)  # Optional details

    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    product= models.ForeignKey(Products,on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




class Book_Breeder(models.Model):
    user=models.ForeignKey(Adopter,on_delete=models.CASCADE)
    breeder=models.ForeignKey(Breeders,on_delete=models.CASCADE)
    description=models.TextField()
    date=models.DateField()
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.status
    

class Chat(models.Model):
    sender=models.CharField(max_length=100,null=True)
    booking = models.ForeignKey(Book_Breeder, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Adopter, on_delete=models.CASCADE, null=True, blank=True)
    breeder = models.ForeignKey(Breeders, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)