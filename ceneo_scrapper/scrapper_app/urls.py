from django.urls import path, re_path

from scrapper_app.views import SelectProductView, ProductView, AddProductView, SelectOpinionView, OpinionView, HomeView, AboutView

urlpatterns = [
    re_path(r'^$', HomeView.as_view()),
    re_path(r'^products\/$', SelectProductView.as_view()),
    re_path(r'^products\/add\/$', AddProductView.as_view()),
    re_path(r'^products\/(?P<product_id>\d+)\/$', ProductView.as_view()),
    re_path(r'^opinions\/$', SelectOpinionView.as_view()),
    re_path(r'^opinions\/(?P<opinion_id>\d+)\/$', OpinionView.as_view()),
    re_path(r'^about\/$', AboutView.as_view()),
]