from django.shortcuts import render
from django.views import View


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
        context = {
            'form': 'not available'
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
