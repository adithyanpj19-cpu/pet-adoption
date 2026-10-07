from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# impoer Q
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')

def user_reg(request):
    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        if not LoginTbl.objects.filter(username=email).exists():
            messages.info(request, "Registration successful")
            log=LoginTbl.objects.create_user(username=email,password=password,usertype='user')
            log.save()
            data=Adopter.objects.create(name=name,address=address,phone=phone,email=email,adopterid=log)
            data.save()
        else:
            messages.error(request, "Email already exists")

    return render(request,'user_reg.html')

# def shelter_reg(request):
#     if request.POST:
#         name=request.POST['name']
#         phone=request.POST['phone']
#         email=request.POST['email']
#         password=request.POST['password']
#         address=request.POST['address']
        
#         if not LoginTbl.objects.filter(username=email).exists():
           
        
#             log=LoginTbl.objects.create_user(username=email,password=password,usertype='shelter')
#             log.save()

#             data=Shelter_staff.objects.create(name=name,phone=phone,email=email,address=address,shelterid=log)
#             data.save()
#             messages.info(request, "Registration successful")
#         else:
#             messages.error(request, "Email already exists")

#     return render(request,'shelter_reg.html')

def veterinary_reg(request):
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']

        if not LoginTbl.objects.filter(username=email).exists():
            log=LoginTbl.objects.create_user(username=email,password=password,usertype='veterinary')
            log.save()

            data=veterinary.objects.create(name=name,phone=phone,email=email,veterinaryid=log)
            data.save()
            messages.info(request, "Registration successful")
        else:
            messages.error(request, "Email already exists")

    return render(request,'veterinary_reg.html')

def trainer_reg(request):
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        proof=request.FILES.get('proof')

        if not LoginTbl.objects.filter(username=email).exists():
            log=LoginTbl.objects.create_user(username=email,password=password,usertype='trainer')
            log.save()

            data=Trainer.objects.create(name=name,phone=phone,email=email,proof=proof,trainerid=log)
            data.save()
            messages.info(request, "Registration successful")
        else:
            messages.error(request, "Email already exists")
    return render(request,'trainer_reg.html')

def shop_reg(request):
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        if not LoginTbl.objects.filter(username=email).exists():
            log=LoginTbl.objects.create_user(username=email,password=password,usertype='shop')
            log.save()

            data=Shop.objects.create(name=name,phone=phone,email=email,address=address,shopid=log)
            data.save()
            messages.info(request, "Registration successful")
        else:
            messages.error(request, "Email already exists")

    return render(request,'shop_reg.html')

def login(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/adminhome')
                elif user.usertype=='user':
                    b=Adopter.objects.get(email=email)
                    request.session["id"]=b.id
                    return redirect('/userhome')
                elif user.usertype=='breeder':
                    u=Breeders.objects.get(email=email)
                    request.session["id"]=u.id
                    return redirect('/breederhome')
                elif user.usertype=='shop':
                    s=Shop.objects.get(email=email)
                    request.session["id"]=s.id
                    return redirect('/shophome')
                
            else:
                messages.error(request,"Login Faild")
                return render(request,"login.html")
        else:
            messages.error(request,"Invalid username or password")
            return render(request,"login.html")
    
    return render(request,'login.html')

def breeder_reg(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        experience=request.POST['breeding_experience']
        specilization=request.POST['breeder_specialization']
        license_number=request.POST['breeder_license']
        password=request.POST['password']
        if not LoginTbl.objects.filter(username=email).exists():
            log=LoginTbl.objects.create_user(username=email,
                                             password=password,
                                             usertype='breeder')
            log.save()
            data=Breeders.objects.create(name=name,
                                        email=email,
                                        phone=phone,
                                        address=address,
                                        experience_years=experience,
                                        specialization=specilization,
                                        license_number=license_number,
                                        created_at=timezone.now(),
                                        user=log)
            data.save()
            messages.info(request,"Registration successful")
        else:
            messages.error(request,"Email already exists")
    return render(request,'breeder_reg.html')

            


def userhome(request):

    return render(request,'userhome.html')

def breederrhome(request):

    return render(request,'breederhome.html')   

def veterinaryhome(request):

    return render(request,'verterinaryhome.html')    

def trainerhome(request):   

    return render(request,'trainerhome.html')
def shophome(request):

    return render(request,'shophome.html')

def shop_product_add(request):
    if request.method == "POST":
        name=request.POST['name']
        brand=request.POST['brand']
        price=request.POST['price']
        quantity=request.POST['quantity']
        image=request.FILES.get('image')
        description=request.POST['description']
        shop_id=request.session['id']
        shop=Shop.objects.get(id=shop_id)
        data=Products.objects.create(name=name,price=price,image=image,description=description,shop_id=shop,brand=brand,quantity=quantity)
        data.save()
        messages.info(request,"Product added successfully")
        return redirect('/shop_product_add')
    products=Products.objects.filter(shop_id=request.session['id'])
    return render(request,'shop_product_add.html',{'products':products})

def shop_product_delete(request,id):
    data=Products.objects.get(id=id)
    data.delete()
    messages.info(request,"Product deleted successfully")
    return redirect('/shop_product_add')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pet, Shop

def shop_pet_add(request):
    shop_id = request.session.get('id')
    if not shop_id:
        messages.error(request, "Shop ID not found in session.")
        return redirect('/shop_pet_add')

    shop = get_object_or_404(Shop, id=shop_id)

    if request.method == "POST":
        pet_id = request.POST.get('pet_id')  # Fetch pet_id for edit functionality
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        color = request.POST.get('color')
        vaccinated = request.POST.get('vaccinated') == 'True'
        image = request.FILES.get('image')
        description = request.POST.get('description')
        health = request.POST.get('health')

        if not all([name, breed, age, gender, color, description, health]):
            messages.error(request, "All fields are required.")
            return redirect('/shop_pet_add')

        if pet_id:  # If pet_id exists, update the existing pet
            pet = get_object_or_404(Pet, id=pet_id, shop_id=shop)
            pet.name = name
            pet.breed = breed
            pet.age = age
            pet.gender = gender
            pet.color = color
            pet.vaccinated = vaccinated
            pet.description = description
            pet.health_status = health
            if image:
                pet.image = image  # Update image only if a new one is provided
            pet.save()
            messages.success(request, "Pet updated successfully.")
        else:  # Otherwise, create a new pet entry
            Pet.objects.create(
                name=name,
                breed=breed,
                age=age,
                gender=gender,
                color=color,
                vaccinated=vaccinated,
                image=image,
                description=description,
                shop_id=shop,
                status='Available',
                health_status=health
            )
            messages.success(request, "Pet added successfully.")

        return redirect('/shop_pet_add')

    pets = Pet.objects.filter(shop_id=shop_id)
    return render(request, 'shop_add_pets.html', {'pets': pets})





def user_product_view(request):
    products = Products.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('id')
        quantity = int(request.POST.get('quantity'))
        user_id = request.session.get('id')

        if not product_id or not quantity:
            messages.error(request, "Invalid product or quantity.")
            return redirect('/user_product_view')

        user = get_object_or_404(Adopter, id=user_id)
        product = get_object_or_404(Products, id=product_id)

        # Get or create an active order for the user
        order, created = Orders.objects.get_or_create(owner=user, status='cart_stage')

        # Try to find the cart item for this product
        cart_item, cart_created = Cart.objects.get_or_create(product=product, order=order, defaults={'quantity': quantity, 'date': timezone.now()})

        if not cart_created:
            # If the product is already in the cart, update the quantity
            cart_item.quantity += quantity
            cart_item.date = timezone.now()
            cart_item.save()

        messages.success(request, "Product added to cart successfully!")
        return redirect('/user_cart_page')

    return render(request, 'user_product_view.html', {'products': products})



def user_pets_view(request):
    # Get filter values from the query parameters
    name = request.GET.get('name', '')
    breed = request.GET.get('breed', '')
    age = request.GET.get('age', '')

    # Start with all pets
    pets = Pet.objects.all()

    # Apply filters if the values are provided
    if name:
        pets = pets.filter(name__icontains=name)  # Case-insensitive search
    if breed:
        pets = pets.filter(breed__icontains=breed)  # Case-insensitive search
    if age:
        pets = pets.filter(age=age)  # Exact match for age

    return render(request, 'user_pets_view.html', {'pets': pets})

def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    uid=request.session['id']
    user=Adopter.objects.get(id=uid)

    if request.method == 'POST':
        living_situation = request.POST['living_situation']
        pet_experience = request.POST['pet_experience']
        employment_status = request.POST['employment_status']
        other_pets_details = request.POST.get('other_pets_details', '')

        # Save the adoption request
        AdoptionRequest.objects.create(
            user=user,
            pet=pet,
            living_situation=living_situation,
            pet_experience=pet_experience,
            employment_status=employment_status,
            other_pets_details=other_pets_details,
            status='Pending',
            created_at=timezone.now()

        )

        messages.success(request, "Your adoption request has been submitted successfully!")
        return redirect('/user_pets_view')

    return render(request, 'adopt_pet.html', {'pet': pet})

def product_add_quantity(request):
    if request.method == "POST":
        id = request.POST.get('id') 
        quantity = request.POST.get('quantity')
        print("id",id)
        print("quantity",quantity)

        if not id or not quantity:
            messages.error(request, "Invalid input! Please provide all details.")
            return redirect('/shop_product_add')

        try:
            product = get_object_or_404(Products, id=id)
            product.quantity += int(quantity)
            product.save()
            messages.success(request, "Quantity added successfully!")
        except ValueError:
            messages.error(request, "Invalid quantity input!")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

        return redirect('/shop_product_add')

    return render(request, 'shop_product_add.html')

def user_cart_page(request):
    user_id=request.session['id']
    user=Adopter.objects.get(id=user_id)
    orders=Orders.objects.filter(owner=user,status='cart_stage').first()
    print(orders)
    cart_items=Cart.objects.filter(order=orders)
    total=0
    for i in cart_items:
        total+=i.product.price*i.quantity

    return render(request,'user_cart_page.html',{'cart_items':cart_items,'total':total,'order':orders})

def remove_from_cart(request):
    cart_id=request.GET['id']
    cart=Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('/user_cart_page')

def user_make_payment(request):
    user_id=request.session['id']
    user=Adopter.objects.get(id=user_id)
    order_id=request.GET['id']
    total=request.GET['total']
    
    if request.method == "POST":
        orders=Orders.objects.get(id=order_id,owner=user)
        orders.status='Payment Confirmed'
        orders.save()
        messages.info(request,"Payment successfull")
        return redirect('/user_cart_page')
    return render(request,'cus_pay.html',{'total':total})



def user_view_bookings(request):
    user_id = request.session.get('id')
    if not user_id:
        messages.error(request, "Please log in first.")
        return redirect('/login')

    user = Adopter.objects.get(id=user_id)
    confirmed_orders = Orders.objects.filter(owner=user, status="Payment Confirmed")

    bookings = []
    for order in confirmed_orders:
        carts = Cart.objects.filter(order=order)
        for cart in carts:
            review = Review.objects.filter(user=user, product=cart.product).first()
            bookings.append({
                'cart': cart,
                'review': review  # If review exists, it will be passed to the template
            })

    return render(request, 'user_view_bookings.html', {'bookings': bookings})


def add_review(request, product_id):
    user_id = request.session.get('id')
    if not user_id:
        messages.error(request, "Please log in first.")
        return redirect('/login')

    user = Adopter.objects.get(id=user_id)
    product = Products.objects.get(id=product_id)

    # Check if the user has already reviewed this product
    existing_review = Review.objects.filter(user=user, product=product).first()
    if existing_review:
        messages.error(request, "You have already reviewed this product.")
        return redirect('/user_bookings')

    if request.method == "POST":
        review_text = request.POST.get('review')
        Review.objects.create(user=user, product=product, review=review_text, created_at=timezone.now())
        messages.success(request, "Review added successfully!")
    
    return redirect('/user_view_bookings')


def user_adoption_request(request):
    uid=request.session['id']
    user=Adopter.objects.get(id=uid)
    user = user
    adoption_requests = AdoptionRequest.objects.filter(user=user).order_by('-created_at')  # Fetching user's requests

    return render(request, 'user_adoption_request.html', {'adoption_requests': adoption_requests})




def manage_adoption_requests(request):
    uid=request.session['id']
    shop=Shop.objects.get(id=uid)
    adoption_requests = AdoptionRequest.objects.filter(pet__shop_id=shop).order_by('-created_at')
    return render(request, 'manage_adoption_requests.html', {'adoption_requests': adoption_requests})

def breeder_adoption_requests(request):
    uid=request.session['id']
    breeder=Breeders.objects.get(id=uid)
    adoption_requests = AdoptionRequest.objects.filter(pet__breeder_id=breeder).order_by('-created_at')
    return render(request, 'breeder_adoption_requests.html', {'adoption_requests': adoption_requests})

def update_adoption_request(request):
    req_id=request.GET['id']
    status=request.GET['status']
    print("status",status)
    req=AdoptionRequest.objects.get(id=req_id)
    req.status=status
    req.save()
    messages.info(request,"Status updated successfully")
    return redirect('manage_adoption_requests')

def update_adoption_requestb(request):
    req_id=request.GET['id']
    status=request.GET['status']
    print("status",status)
    req=AdoptionRequest.objects.get(id=req_id)
    req.status=status
    req.save()
    messages.info(request,"Status updated successfully")
    return redirect('breeder_adoption_requests')



def breeder_add_pet(request):
    breeder_id = request.session['id']
    breeder = Breeders.objects.get(id=breeder_id)
    
    if request.method == "POST":
        pet_id = request.POST.get('pet_id')  # Fetch pet ID if editing
        name = request.POST['name']
        breed = request.POST['breed']
        age = request.POST['age']
        gender = request.POST['gender']
        color = request.POST['color']
        vaccinated = request.POST['vaccinated']
        image = request.FILES.get('image')
        description = request.POST['description']
        health = request.POST['health']
        
        if pet_id:
            # Update existing pet
            pet = Pet.objects.get(id=pet_id, breeder_id=breeder)
            pet.name = name
            pet.breed = breed
            pet.age = age
            pet.gender = gender
            pet.color = color
            pet.vaccinated = vaccinated
            pet.description = description
            pet.health_status = health
            if image:
                pet.image = image
            pet.save()
            messages.success(request, "Pet updated successfully.")
        else:
            # Create new pet
            Pet.objects.create(
                name=name,
                breed=breed,
                age=age,
                gender=gender,
                color=color,
                vaccinated=vaccinated,
                image=image,
                description=description,
                breeder_id=breeder,
                health_status=health
            )
            messages.success(request, "Pet added successfully.")
        
        return redirect('/breeder_add_pet')
    
    pets = Pet.objects.filter(breeder_id=breeder)
    return render(request, 'breeder_add_pet.html', {'pets': pets})


def requester_data(request):
    req_id=request.GET['id']
    req=AdoptionRequest.objects.get(id=req_id)
    print(req)
    return render(request,'requester_data.html',{'request':req})


def breeder_chat(request):
    hid = request.session['id']
    uid = request.GET['uid']
    bid = request.GET['bid']

    user = Adopter.objects.get(id=uid)
    breeder = Breeders.objects.get(id=hid)
    booking=Book_Breeder.objects.get(id=bid)
    if request.method == "POST":  
        message = request.POST['msg']
        Chat.objects.create(sender='breeder',booking=booking, user=user, breeder=breeder, message=message)
    chat = Chat.objects.filter(Q(user=user) | Q(breeder=breeder), booking=booking).order_by('created_at')
    return render(request, 'breeder_chat.html', {'chats': chat, 'booking': booking})

def user_chat(request):
    uid=request.session['id']
    bid= request.GET['bid']
    rid=request.GET['rid']
    user = Adopter.objects.get(id=uid)
    breeder = Breeders.objects.get(id=rid)
    booking=Book_Breeder.objects.get(id=bid)
    if request.method == "POST":  
        message = request.POST['msg']
        Chat.objects.create(sender='user',booking=booking, user=user, breeder=breeder, message=message)
    chat = Chat.objects.filter(Q(user=user) | Q(breeder=breeder), booking=booking).order_by('created_at')
    return render(request, 'user_chat.html', {'chats': chat, 'booking': booking})

def user_view_breeders(request):
    breeders = Breeders.objects.all()
    if request.method == 'POST':
        breeder_id=request.POST['breeder_id']
        description=request.POST['description']
        user_id=request.session['id']
        user=Adopter.objects.get(id=user_id)
        breeder=Breeders.objects.get(id=breeder_id)
        book_breeder=Book_Breeder.objects.create(user=user,breeder=breeder,description=description,status='Pending',date=timezone.now())
        book_breeder.save()
        messages.info(request,"Booking request sent successfully")
        return redirect('/user_view_breeders')
    return render(request, 'user_view_breeders.html', {'breeders': breeders})



def user_breeder_bookings(request):
    user_id = request.session.get('id') 
    bookings = Book_Breeder.objects.filter(user_id=user_id).select_related('breeder')

    return render(request, 'user_breeder_bookings.html', {'bookings': bookings})



def breeder_booking_requests(request):
    breeder_id = request.session.get('id')  # Assuming breeder is stored in session
    bookings = Book_Breeder.objects.filter(breeder_id=breeder_id)
    return render(request, 'breeder_booking_request.html', {'bookings': bookings})

def update_booking_status(request, booking_id, status):
    try:
        booking = Book_Breeder.objects.get(id=booking_id)
        booking.status = status
        booking.save()
        messages.success(request, f"Booking has been {status.lower()} successfully.")
    except Book_Breeder.DoesNotExist:
        messages.error(request, "Booking not found.")

    return redirect('/breeder_booking_requests')


def adminhome(request):
    return render(request,'adminhome.html')

def admin_view_users(request):
    users = Adopter.objects.all()
    return render(request, 'admin_view_users.html', {'users': users})

def user_update_status(request):
    uid=request.GET['id']
    status=request.GET['status']
    print("status",status)
    user=Adopter.objects.get(id=uid)
    user.adopterid.is_active=status
    user.adopterid.save()
    messages.info(request,"Status updated successfully")
    return redirect('admin_view_users')

def admin_view_breeders(request):
    breeders = Breeders.objects.all()
    return render(request, 'admin_view_breeders.html', {'breeders': breeders})

def breeder_update_status(request):
    uid=request.GET['id']
    status=request.GET['status']
    print("status",status)
    breeder=Breeders.objects.get(id=uid)
    breeder.user.is_active=status
    breeder.user.save()
    messages.info(request,"Status updated successfully")
    return redirect('admin_view_breeders')

def admin_view_shops(request):
    shops = Shop.objects.all()
    return render(request, 'admin_view_shop.html', {'shops': shops})

def shop_update_status(request):
    uid=request.GET['id']
    status=request.GET['status']
    print("status",status)
    shop=Shop.objects.get(id=uid)
    shop.shopid.is_active=status
    shop.shopid.save()
    messages.info(request,"Status updated successfully")
    return redirect('admin_view_shops')





