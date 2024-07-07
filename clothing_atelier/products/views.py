from django.http import HttpRequest
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from .models import Collection, Product, Supplier, Fabric, Second_layer, Lace, Accessories, Glitter


def product_view(request: HttpRequest):
    products = (
        Product
        .objects
        .select_related("collection")
        .all()
    )
    context = {
        "products": products,
    }
    return render(
        request, "products/products-list.html",
        context,
    )

def collection_with_product(request: HttpRequest):
    return render()


class CollectionListViews(ListView):
    model = Collection


class CollectionDetailView(DetailView):
    model = Collection


class CreateConsumableView(View):
    template_name = "products/create_consumable.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        consumable_type = request.POST.get("consumable_type")
        if consumable_type:
            return redirect(reverse(f"products:create_{consumable_type}"))
        return render(request, self.template_name)


class FabricDetailView(DetailView):
    model = Fabric


class FabricCreateView(CreateView):
    model = Fabric
    fields = "__all__"
    template_name = "products/fabric_form.html"
    success_url = reverse_lazy("products:consumable_list")


class Second_layerDetailView(DetailView):
    model = Second_layer


class Second_layerCreateView(CreateView):
    model = Second_layer
    fields = "__all__"
    template_name = "products/second_layer_form.html"
    success_url = reverse_lazy("products:consumable_list")


class AccessoriesDetailView(DetailView):
    model = Accessories


class AccessoriesCreateView(CreateView):
    model = Accessories
    fields = "__all__"
    template_name = "products/accessories_form.html"
    success_url = reverse_lazy("products:consumable_list")


class GlitterDetailView(DetailView):
    model = Glitter


class GlitterCreateView(CreateView):
    model = Glitter
    fields = "__all__"
    template_name = "products/glitter_form.html"
    success_url = reverse_lazy("products:consumable_list")


class LaceDetailView(DetailView):
    model = Lace


class LaceCreateView(CreateView):
    model = Lace
    fields = "__all__"
    template_name = "products/lace_form.html"
    success_url = reverse_lazy("products:consumable_list")


def consumable_list(request):
    fabrics = Fabric.objects.all()
    second_layers = Second_layer.objects.all()
    accessories = Accessories.objects.all()
    glitters = Glitter.objects.all()
    laces = Lace.objects.all()
    context = {
        "fabrics": fabrics,
        "second_layers": second_layers,
        "accessories": accessories,
        "glitters": glitters,
        "laces": laces,
    }
    return  render(
        request,
        "products/consumable_list.html",
        context,
    )
