import json
import os
import markdown

from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.conf import settings

from scrapper_app.form import AddProductForm
from scrapper_app.analyzer import analyze_product, get_charts
from scrapper_app.models import ProductModel, OpinionModel
from scrapper_app.scraper import get_opinions, get_product


class HomeView(View):

    def get(self, request):
        with open(os.path.join(settings.BASE_DIR, 'requirements.txt')) as file:
            context = {
                'dependencies': [req[:-2] for req in file.readlines()]
            }

        return render(request, 'home.html', context=context)


class AboutView(View):

    def get(self, request):
        with open(os.path.join(os.path.dirname(settings.BASE_DIR), 'README.md')) as file:
            md = markdown.Markdown()
            context = {
                'md': md.convert(file.read())
            }

        return render(request, 'about.html', context=context)


class SelectProductView(View):

    def get(self, request):
        search = request.GET.get('search')
        if search:
            products = ProductModel.objects.filter(name__icontains=search)
        else:
            products = ProductModel.objects.all()
        context = {
            'products': products,
            'search': search,
        }
        return render(request, 'select_product.html', context=context)


class AddProductView(View):

    def get(self, request):
        form = AddProductForm()
        products = ProductModel.objects.all()
        context = {
            'form': form,
            'products': products,
        }
        return render(request, 'add_product.html', context=context)

    def post(self, request):
        form = AddProductForm(request.POST)

        if form.is_valid():
            product_id = form.cleaned_data.get('product_id')
            product = get_product(product_id)
            if product:  # product exists in Ceneo system
                get_opinions(product)
                get_charts(product)
                return redirect(reverse('product', kwargs={'product_id': product_id}))
            else:  # product with this id doesn't exist
                form.add_error('product_id', 'Produkt o podanym ID nie istnieje.')

        context = {
            'form': form
        }

        return render(request, 'add_product.html', context=context)


class ProductView(View):

    def get(self, request, product_id):
        product = get_object_or_404(ProductModel, product_id=product_id)
        analysis = analyze_product(product)

        context = {
            'product': product,
        }

        context.update(analysis)

        return render(request, 'product.html', context=context)


class DownloadView(View):

    def get(self, request, product_id):
        product = get_object_or_404(ProductModel, product_id=product_id)
        opinions = OpinionModel.objects.filter(product=product)

        data = serializers.serialize('json', opinions)

        response = HttpResponse(json.dumps(json.loads(data), indent=4, ensure_ascii=False), content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename="opinions-{product_id}.json"'

        return response


class SelectOpinionView(View):

    def get(self, request):
        opinions = OpinionModel.objects.all()

        context = {
            'opinions': opinions,
        }

        return render(request, 'select_opinion.html', context=context)


class OpinionView(View):

    def get(self, request, opinion_id):
        opinion = OpinionModel.objects.get(opinion_id=opinion_id)

        context = {
            'opinion': opinion,
            'opinion_json': json.loads(serializers.serialize('json', [opinion, ], fields=['id', 'opinion_id', 'author', 'recommendation', 'stars', 'content', 'cons', 'pros', 'useful', 'useless', 'opinion_date', 'purchase_date']))[0],
        }

        return render(request, 'opinion.html', context=context)
