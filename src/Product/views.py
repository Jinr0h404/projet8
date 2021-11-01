from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Product.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def search(request):
    query = request.GET.get('query')
    products_list = Product.objects.filter(product_name__icontains=query)
    print(products_list)
    paginator = Paginator(products_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for o in page_obj:
        print (o)
    print("et maintenant la page 2")
    #page_obj = paginator.get_page(page)
    for o in page_obj:
        print(o)
    context = {
        'page_obj': page_obj,
        'nom_produit': page_obj,
        'paginate':True,
        "query":query,
    }
    return render(request, 'product/search.html', context)

def substitute_getter(id_product):
    produit = Product.objects.get(pk=id_product)
    list_brut = Product.objects.filter(category__in=produit.category.all())
    list_order_value = []
    for prod in list_brut:
        list_order_value.append(prod.pk)

    def count_to_dict(lst):
        return {k: lst.count(k) for k in
                lst}

    list_count_common = count_to_dict(list_order_value)
    valeur_sub = sorted(list_count_common.items(), key=lambda x: x[1], reverse=True)
    return valeur_sub

def search_substitute(request):
    query = request.GET.get('query')
    query_id = Product.objects.filter(pk=query)
    print(query)
    print(query_id)
    #prod_id = query_id.pk
    products_tuple = substitute_getter(query)
    products_list = []
    for i in products_tuple:
        products_list.append(Product.objects.get(pk=i[0]))
    print(products_list)
    #products_list = Product.objects.get(pk=query)
    title = "Résultats pour la requête %s"%query
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #try:
    #page_obj = paginator.get_page(page_number)
    #except PageNotAnInteger:
        #product = paginator.page(1)
    #except EmptyPage:
        #product = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
        'nom_produit': page_obj,
        'paginate': True,
        'query':query,
    }
    return render(request, 'product/search_substitute.html', context)