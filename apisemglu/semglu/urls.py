from email.mime import base
from django.urls import re_path, path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf import settings

from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Listas
_path = "api/list/"

router.register(_path + r"product", views.ProductList, basename="product-list")
router.register(_path + r"safety", views.SafetyList, basename="safety-list")
router.register(_path + r"report", views.ReportList, basename="report-list")
router.register(_path + r"review", views.ReviewList, basename="review-list")
router.register(_path + r"brand", views.BrandList, basename="brand-list")

# Detalhes
_path = "api/detail/"

router.register(
    _path + r"report/(?P<idReport>[^/.]+)",
    views.ReportDetail,
    basename="report-detail",
)
router.register(
    _path + r"safety/(?P<idSafety>[^/.]+)",
    views.SafetyDetail,
    basename="safety-detail",
)
router.register(
    _path + r"review/(?P<idReview>[^/.]+)",
    views.ReviewDetail,
    basename="review-detail",
)
router.register(
    _path + r"brand/(?P<idBrand>[^/.]+)", views.BrandDetail, basename="brand-detail"
)
router.register(
    _path + r"product/(?P<barCode>[^/.]+)",
    views.ProductDetail,
    basename="product-detail",
)

urlpatterns = [
    re_path(r"^", include(router.urls)),
    re_path(
        r"^api/productInfos/(?P<barCode>[^/.]+)", views.ProductJoinedDetails.as_view()
    ),
    # re_path(r"^api/media/(?P<path>[^/.]+)", views.FileView.as_view(path)),
]


def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, str(document_root), show_indexes)


urlpatterns += [
    re_path(
        r"^api/media/(?P<path>[^/.]+)",
        protected_serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
