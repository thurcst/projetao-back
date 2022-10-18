from django.urls import re_path, path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    # Exemplo de como foram construídas as urls:
    # r'^products/$' retorna a lista completa de todos os produtos
    # r'^product/(?P<barCode>.+)/$' retorna o produto individual
    #    (?P<barCode>.+) busca a chave primária (no caso o barCode)

    # Listas
    re_path(r"^api/list/user/$", views.UserList.as_view()),
    re_path(r"^api/list/safety/$", views.SafetyList.as_view()),
    re_path(r"^api/list/report/$", views.ReportList.as_view()),
    re_path(r"^api/list/product/$", views.ProductList.as_view(), name="product-list"),
    re_path(r"^api/list/brand/$", views.BrandList.as_view()),
    re_path(r"^api/list/review/$", views.ReviewList.as_view()),

    # Detalhes
    re_path(
        r"^api/detail/product/(?P<barCode>.+)/$",
        views.ProductDetail.as_view(),
        name="product-detail",
    ),
    re_path(
        r"^api/detail/productInfos/(?P<barCode>.+)/$",
        views.ProductJoinedDetails.as_view(),
        name="product-infos",
    ),
    re_path(r"^api/detail/user/(?P<idUser>.+)/$", views.UserDetail.as_view()),
    re_path(r"^api/detail/safety/(?P<idSafety>.+)/$", views.SafetyDetail.as_view()),
    re_path(r"^api/detail/report/(?P<idReport>.+)/$", views.ReportDetail.as_view()),
    re_path(r"^api/detail/brand/(?P<idBrand>.+)/$", views.BrandDetail.as_view()),
    re_path(r"^api/detail/review/(?P<idReview>.+)/$", views.ReviewDetail.as_view()),

    re_path(r"^testTokens/", views.testView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
