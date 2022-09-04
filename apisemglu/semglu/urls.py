from django.urls import path
from . import views

urlpatterns = [
    path(r'products/', views.ProductList.as_view(), name='product-list'),
    path(r'product/<int:barCode>', views.ProductDetail.get_pkey, name='product-detail'),

    path(r'users/', views.UserList.as_view()),
    path(r'user/<int:idUser>', views.UserDetail.get_pkey),

    path(r'safetys/', views.SafetyList.as_view()),
    path(r'safety/<str:idSafety>', views.SafetyDetail.get_pkey),

    path(r'reports/', views.ReportList.as_view()),
    path(r'report/<int:idReport>', views.ReportDetail.get_pkey),

    path(r'brands/', views.BrandList.as_view()),
    path(r'brand/<int:idBrand>', views.BrandDetail.get_pkey)
]