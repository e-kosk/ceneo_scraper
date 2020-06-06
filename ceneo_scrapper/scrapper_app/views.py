from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from scrapper_app.form import AddProductForm
from scrapper_app.models import ProductModel


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


class SelectProductView(View):

    def get(self, request):
        return render(request, 'select_product.html')


class AddProductView(View):

    def get(self, request):
        form = AddProductForm()
        context = {
            'form': form
        }
        return render(request, 'add_product.html', context=context)

    def post(self, request):
        form = AddProductForm(request.POST)

        if form.is_valid():
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, 'add_product.html', context=context)


class ProductView(View):

    def get(self, request, product_id):
        return render(request, 'product.html')


class SelectOpinionView(View):

    def get(self, request):
        return render(request, 'select_opinion.html')


class OpinionView(View):

    def get(self, request, opinion_id):
        return render(request, 'opinion.html')
