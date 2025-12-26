from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ItemSerializer
from rest_framework. permissions import IsAuthenticated, AllowAny
from food.models import Item
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    permission_classes=[AllowAny]


# def index(request):
#     item_list = Item.objects.all().order_by('-id')

#     food_name = request.GET.get('food_name')
#     if food_name != "" and food_name is not None:
#         item_list = item_list.filter(item_name__icontains=food_name)

#     paginator = Paginator(item_list, 3)
#     page = request.GET.get('page')
#     item_list = paginator.get_page(page)
#     context = {
#         "item_list": item_list,
#         "food_name": food_name,

#     }
#     return render(request, "food/index.html", context)


class ItemListCreate(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Item.objects.filter(author=user)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class ItemDelete(generics.DestroyAPIView):
    # queryset= Item.objects.all()
    serializer_class=ItemSerializer
    permission_classes=[IsAuthenticated]    
    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(author=user)
