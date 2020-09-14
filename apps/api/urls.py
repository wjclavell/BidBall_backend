# from django.urls import path, include
# from django.conf.urls import url
# from rest_framework import routers
# from apps.api.views import CategoryViewSet, CategoryRecipes, SingleCategoryRecipe, RecipesViewSet
#
# router = routers.DefaultRouter()
# router.register('categories', CategoryViewSet, basename='categories')
# router.register('recipes', RecipesViewSet, basename='recipes')
#
# custom_urlpatters = [
#     # Regex Syntax: r -> starting regex, ?P -> parameter, \d+ -> number, $ -> end of regex
#     url(r'categories/(?P<category_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
#     url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', SingleCategoryRecipe.as_view(),
#         name='single_category_recipes')
# ]
#
# urlpatterns = router.urls
# urlpatterns += custom_urlpatters

# urlpatterns = [
#     path('', include(router.urls))
# ]
