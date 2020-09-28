from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Theme, Metal, Review
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    themes = None
    metals = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'theme' in request.GET:
            themes = request.GET['theme'].split(',')
            products = products.filter(theme__name__in=themes)
            themes = Theme.objects.filter(name__in=themes)

        if 'metal' in request.GET:
            metals = request.GET['metal'].split(',')
            products = products.filter(metal__name__in=metals)
            metals = Metal.objects.filter(name__in=metals)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_themes': themes,
        'current_metals': metals,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    reviews = product.reviews.all()

    context = {
        'product': product,
        'reviews': reviews
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def review_product(request, product_id):
    """ Add a review to the product_detail page """
    product = get_object_or_404(Product, pk=product_id)
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.user.is_authenticated:
            try:
                form_data = {
                    'user': profile,
                    'product': product,
                    'rating': request.POST['rating'],
                    'description': request.POST['description'],
                    'visible': True
                }
                review_form = ReviewForm(form_data)
                if review_form.is_valid():
                    review_form.save()
                    messages.success(request, 'Successfully reviewed this product!')
                    return redirect(
                        reverse('product_detail', args=[product.id]))
                else:
                    messages.error(request, f'Failed to review {product.name}. Please ensure the form is valid.')

            except UserProfile.DoesNotExist:
                review_form = ReviewForm()
        else:
            messages.error(request, f'Please Login to review {product.name}')
            return redirect(reverse('product'))

    else:
        review_form = ReviewForm()

    template = 'products/review_product.html'
    context = {
        'review_form': review_form,
        'product': product,
        'user': profile,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Edit a review """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    if not request.user == review.user.user:
        messages.error(request, 'Sorry, only the user who wrote the review can do that.')
        return redirect(reverse('product_detail', args=[product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing you review for {product.name}')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'product': product,
        'review': review
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a product from the store """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    if not request.user == review.user.user:
        messages.error(request, 'Sorry, only the user who wrote the review can do that.')
        return redirect(reverse('product_detail', args=[product.id]))

    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
