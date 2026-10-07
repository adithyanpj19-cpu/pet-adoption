from django.contrib import admin
from pet_app.models import *

# Register your models here.
#register the models
admin.site.register(Adopter)
# admin.site.register(Shelter_staff)
# admin.site.register(veterinary)
# admin.site.register(Trainer)
admin.site.register(Shop)
admin.site.register(LoginTbl)
admin.site.register(Products)
admin.site.register(Pet)
admin.site.register(AdoptionRequest)
admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Chat)

