from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse

from adminapp.forms import ProductCategoryCreateForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'пользователи/создания'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()
    context = {
        'title': title,
        'user_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)


def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)



    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=edit_user )
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserEditForm(instance=edit_user)


    context = {
        'title': title,
        'update_form': edit_form
    }

    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))


    context = {
        'title': title,
        'user_to_delete': user
    }

    return render(request, 'adminapp/user_delete.html', context)


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


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


def product_create(request, pk):
    title = 'продукт/создания'


def product_read(request, pk):
    title = 'продукт/чтение'


def product_update(request, pk):
    title = 'продукт/редактирование'


def product_delete(request, pk):
    title = 'продукт/удаление'