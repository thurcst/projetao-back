from rest_framework import filters

# Filtro dos usuarios
class FiltroUser(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.query_params.getlist('search_fields', [
            # Campos de pesquisa do usuário
            'idUser',
            'nick'
        ])

# Filtro das safeties
class FiltroSafety(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.query_params.getlist('search_fields', [
            # Campos de pesquisa das safeties
            'idSafety',
            'category',
            'description'
        ])

# Filtro dos reports
class FiltroReport(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.query_params.getlist('search_fields', [
            # Campos de pesquisa dos laudos
            'idReport'
        ])

# Filtro das marcas
class FiltroBrand(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.query_params.getlist('search_fields', [
            # Campos de pesquisa das marcas
            'idBrand',
            'brandName',
            'contact'
        ])

# Filtro dos produtos
class FiltroProduct(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.query_params.getlist('search_fields', [
            # Campos de pesquisa dos produtos
            'barCode',
            'idBrand',
            'idSafety',
            'idReport',
            'productName',
            'productCategory',
            'productIngredients'
        ])
