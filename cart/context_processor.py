from .models import cartlist, items
from .views import c_id  # Import the correct function

def count(request):
    item_count = 0  # Initialize item_count inside function

    if "admin" in request.path:
        return {}  # Return an empty dictionary if in admin panel

    try:
        ct = cartlist.objects.get(cart_id=c_id(request))  # Get the cartlist
        cti = items.objects.filter(cart=ct)  # Get items from cart
        for c in cti:
            item_count += c.quan  # Count quantity of all items
    except cartlist.DoesNotExist:
        item_count = 0  # If cart does not exist, set count to 0

    return {'itc': item_count}  # ✅ Correctly return the dictionary
