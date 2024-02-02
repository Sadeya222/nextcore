from django.shortcuts import render
from store.models import Product, ReviewRating, BannerImage

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    
    images = BannerImage.objects.all()[:3]
    
    context = {
    'products': products,
    'reviews': reviews,
    'images': images,
}
 
    return render(request, 'home.html', context)

        
        



