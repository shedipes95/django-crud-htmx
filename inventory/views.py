from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product
from .forms import ProductForm, OrderForm

# List + HTMX search + Order form
def product_list(request):
    q = request.GET.get("q", "").strip()
    products = Product.objects.all().order_by("-created_at")
    if q:
        products = products.filter(Q(name__icontains=q) | Q(sku__icontains=q))

    # If the request is from HTMX, return only table rows (partial)
    if request.headers.get("Hx-Request"):
        return render(request, "inventory/partials/_product_rows.html", {"products": products})

    return render(request, "inventory/product_list.html", {
        "products": products,
        "q": q,
        "order_form": OrderForm(),
    })

# Create / Update / Delete Product

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "inventory/product_form.html", {"form": form, "title": "New Product"})


def product_update(request, pk):
    p = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=p)
    return render(request, "inventory/product_form.html", {"form": form, "title": "Edit Product"})


def product_delete(request, pk):
    p = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        p.delete()
        return redirect("product_list")
    return render(request, "inventory/product_confirm_delete.html", {"product": p})

# Order creation (POST). Decrease stock if valid.
from django.views.decorators.http import require_POST

@require_POST
def order_create(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        product = order.product
        product.stock -= order.quantity
        product.save()
        order.save()
        # Optional: HTMX-friendly confirmation snippet
        if request.headers.get("Hx-Request"):
            return render(request, "inventory/partials/_order_success.html", {"order": order})
        return redirect("product_list")
    # On error, return to list with errors
    products = Product.objects.all().order_by("-created_at")
    return render(request, "inventory/product_list.html", {"products": products, "order_form": form})