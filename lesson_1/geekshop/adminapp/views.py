from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy

from adminapp.forms import ProductCategoryCreateForm, ProductCategoryEditForm, ProductEditForm, ProductCreateForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class UsersListView(LoginRequiredMixin,ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    login_url = '/'

    def get_context_data(self,*,object_list=None,**kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'
        return context

    # def get(self,request,*args,**kwargs):
    #     get_con = super(UsersListView, self).get()
    #     return get_con
# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context)

class UsersCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')

# def user_create(request):
#     title = 'пользователи/создания'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#     context = {
#         'title': title,
#         'user_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)

class UsersUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserRegisterForm # CBV 
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_staff:users')


# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#
#
#
#     if request.method == 'POST':
#         edit_form = ShopUserEditForm(request.POST, request.FILES, instance=edit_user )
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserEditForm(instance=edit_user)
#
#
#     context = {
#         'title': title,
#         'update_form': edit_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)

class UsersDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
    # def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin_staff:users'))
#
#
#     context = {
#         'title': title,
#         'user_to_delete': user
#     }
#
#     return render(request, 'adminapp/user_delete.html', context)


def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


def category_create(request):
    title = 'категории/создания'


    if request.method == 'POST':
        category_form = ProductCategoryCreateForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin_staff:categories'))

    else:
        category_form = ProductCategoryCreateForm()
    context = {
        'title': title,
        'category_form': category_form
    }

    return render(request, 'adminapp/category_update.html', context)

def category_update(request, pk):
    title = 'категории/редактирование'

    category_edit = get_object_or_404(ProductCategory,pk=pk)

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category_edit)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin_staff:category_update',args= [category_edit.pk]))

    else:
        category_form = ProductCategoryEditForm(instance=category_edit)
    context = {
        'title': title,
        'category_form': category_form
    }

    return render(request, 'adminapp/category_update.html', context)

def category_delete(request, pk):
    title = 'категории/удаление'

    category_del = get_object_or_404(ProductCategory,pk=pk)

    if request.method == 'POST':
        category_del.is_active = False
        category_del.save()
        return HttpResponseRedirect(reverse('admin_staff:categories'))


    context = {
        'title':title,
        'category_del':category_del,
    }
    return render(request,'adminapp/category_delete.html', context)


def products(request, pk=None):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_create(request, pk):
    title = 'продукт/создания'

    if request.method == 'POST':
        product_form = ProductCreateForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products' ,args=[pk]))

    else:
        product_form = ProductCreateForm()
    context = {
        'title': title,
        'product_form': product_form
    }

    return render(request, 'adminapp/product_update.html', context)

def product_read(request, pk):
    title = 'продукт/чтение'

    product = get_object_or_404(Product, pk=pk)
    context = {'title': title, 'object': product }

    return render(request, 'adminapp/product_read.html', context)



def product_update(request, pk):
    title = 'продукт/редактирование'

    product_edit = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES, instance=product_edit)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:product_update', args=[product_edit.pk]))

    else:
        product_form = ProductEditForm(instance=product_edit)
    context = {
        'title': title,
        'product_form': product_form,
    }

    return render(request, 'adminapp/product_update.html', context)

def product_delete(request, pk):
    title = 'продукт/удаление'

    product_del = get_object_or_404(Product,pk=pk)

    if request.method == 'POST':
        product_del.is_active = False
        product_del.save()
        return HttpResponseRedirect(reverse('admin_staff:products', args=[product_del.category_id]))


    context = {
        'title':title,
        'product_del':product_del,
    }
    return render(request,'adminapp/product_delete.html', context)