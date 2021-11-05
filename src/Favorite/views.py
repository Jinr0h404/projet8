from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Favorite.models import Favorites
from User.models import CustomUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Product.models import Product

# Create your views here.
@login_required
def index(request):
    user_connected = CustomUser.objects.get(pk=request.user.id)
    query_list = Favorites.objects.filter(user_id=user_connected)
    products_list= []
    substitute_product = []
    bad_product = []
    all_product = Product.objects.all()

    for i in query_list:
        print(i.product_id_id)
        print(i.substitute_id_id)
        print(i.id)
        substitute_product.append((i.substitute_id_id, i.product_id_id))
        bad_product.append(Product.objects.get(pk=i.product_id_id))
        products_list.append(Product.objects.get(pk=i.substitute_id_id))
    print(products_list)
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'nom_produit': page_obj,
        'paginate': True,
        'substitute_product':substitute_product,
        'bad_product': bad_product,
        'all_product': all_product,
    }

    return render(request, "Favorite/index.html", context)