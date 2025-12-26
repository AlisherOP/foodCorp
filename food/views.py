from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView  # for the class base view
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from users.models import Profile
from rest_framework import viewsets, generics
from .serializers import RoomSerializer
# Create your views here.


class RoomView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = RoomSerializer
# out of stock


def index(request):
    item_list = Item.objects.all().order_by('-id')
    
    food_name = request.GET.get('food_name')
    if food_name != "" and food_name is not None:
        item_list = item_list.filter(item_name__icontains=food_name)

    paginator = Paginator(item_list, 3)
    page = request.GET.get('page')
    item_list = paginator.get_page(page)
    context = {
        "item_list": item_list,
        "food_name": food_name,

    }
    return render(request, "food/index.html", context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

# ghost


def item(request):
    return HttpResponse("This is an item view")


def detail(request, item_id):
    # we are only calling the item with this id
    item = Item.objects.get(pk=item_id)
    context = {
        "item": item,
    }
    return render(request, "food/detail.html", context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    # context_object_name='item'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})

# class based for item


class CreateItem(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    template_name = "food/item-form.html"

    def form_valid(self, form):  # accepting form
        form.instance.user_name = self.request.user  # getting the username for the form
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item-form.html", {"form": form, "item": item})


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == "POST":  # deleting specific item
        item.delete()
        return redirect("food:index")

    return render(request, "food/item-delete.html", {"item": item})




def food_detail(request, pk):
    food = get_object_or_404(Item, pk=pk)
    is_favorite = False

    if request.user.is_authenticated:
        user_profile = Profile.objects.filter(
            user=request.user).first()
        if user_profile:
            is_favorite = user_profile.is_favorite(food)

    return render(request, 'food/section.html', {
        'food': food,
        'is_favorite': is_favorite
    })


