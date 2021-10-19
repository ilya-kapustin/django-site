from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView
from .models import Shops, ShopsGroup, ShopContacts, ShopsComm, Tag
from django.urls import reverse_lazy
from .forms import AddShop, AddGroup, AddComm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from cart.forms import CartAddProductForm
from django.views.generic.list import MultipleObjectMixin
from django.core import serializers


class Contacts(generic.ListView):
    model = ShopContacts
    template_name = 'shops_index/contacts.html'
    context_object_name = 'contacts'

    def get_context_data(self, *args, **kwargs):
        context = super(Contacts, self).get_context_data(**kwargs)
        context['title'] = "Контакты"
        return context


class ShopIndex(generic.ListView):
    model = Shops
    template_name = 'shops_index/shops_index.html'
    context_object_name = 'things'
    queryset = Shops.objects.order_by('?')

    def get_context_data(self, *args, **kwargs):
        context = super(ShopIndex, self).get_context_data(**kwargs)
        context['title'] = "Магазин бесплатных объявлений"
        return context


class ShopIndexDetailView(generic.DetailView):
    model = Shops
    template_name = 'shops_index/shops_index_detail.html'
    context_object_name = 'thing'

    def get_context_data(self, *args, **kwargs):
        form = AddComm()
        context = super(ShopIndexDetailView, self).get_context_data(**kwargs)
        context['comm'] = ShopsComm.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        context['form'] = form
        return context

    @method_decorator(permission_required('shops_index.add_shopscomm'))
    def post(self, request, pk):
        form = AddComm(request.POST)
        if form.is_valid():
            ShopsComm.objects.create(**form.cleaned_data)
        else:
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')


class About(TemplateView):
    template_name = 'shops_index/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        return context


class AllGroup(generic.ListView):
    model = ShopsGroup
    template_name = 'shops_index/categories.html'
    context_object_name = 'group'
    queryset = ShopsGroup.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(AllGroup, self).get_context_data(**kwargs)
        context['title'] = "Гуппы товаров"
        return context


class GroupDetailView(generic.DetailView, MultipleObjectMixin):  # MultipleObjectMixin
    model = ShopsGroup
    template_name = 'shops_index/group_detail.html'
    context_object_name = 'group'
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        object_list = Shops.objects.filter(group=self.get_object())
        context = super(GroupDetailView, self).get_context_data(object_list=object_list,
                                                                **kwargs)  # object_list=object_list,
        context['things'] = Shops.objects.all()
        return context


def add_shops(request):
    if request.method == 'POST':
        form = AddShop(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddShop()
    return render(request, 'shops_index/add_shops.html',
                  {'form': form, 'title': 'Добавление объявления'})


def add_group(request):
    if request.method == 'POST':
        form = AddGroup(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('/')
    else:
        form = AddGroup()
    return render(request, 'shops_index/add_group.html',
                  {'form': form, 'title': 'Добавление объявления'})


class GroupUpdate(generic.UpdateView):
    model = ShopsGroup
    template_name = 'shops_index/group_update.html'
    fields = ['name', 'description', 'img']


class ShopsUpdate(generic.UpdateView):
    model = Shops
    template_name = 'shops_index/shops_update.html'
    fields = ['title', 'code_thing', 'img', 'description', 'price', 'group']


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'shops_index/tag.html', {'tags': tags})


def tags_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    return render(request, 'shops_index/tag_detail.html', {'tag': tag})


def get_group_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, ShopsGroup.objects.all())
    return HttpResponse(data)

def get_shops_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, Shops.objects.all())
    return HttpResponse(data)
