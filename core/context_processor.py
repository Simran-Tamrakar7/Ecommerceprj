from ast import Add
from core.models import Product,Category,Vendor, CartOrder, CartOrderItems,ProductImages, ProductReview, wishlist, Address
from django.db.models import Min, Max

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price=Product.objects.aggregate(Min("price"), Max("price"))


    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None
        
    return{
        'categories':categories,
        'vendors':vendors,
        'address':address,
        'min_max_price':min_max_price,
    }
