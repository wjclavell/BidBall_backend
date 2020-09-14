from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import GameViewSet, BidViewSet

router = routers.DefaultRouter()
router.register('games', GameViewSet, basename='games')
router.register('bids', BidViewSet, basename='bids')

# custom_urlpatterns = [
#     # Regex Syntax: r -> starting regex, ?P -> parameter, \d+ -> number, $ -> end of regex
#     url(r'categories/(?P<category_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
#     url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', SingleCategoryRecipe.as_view(),
#         name='single_category_recipes')
# ]
#
# urlpatterns = router.urls
# urlpatterns += custom_urlpatterns

urlpatterns = [
    path('', include(router.urls))
]
