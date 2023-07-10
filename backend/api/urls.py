from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()

router.register('users', views.CustomUserViewSet, basename='users')
router.register('recipes', views.RecipeViewSet, basename='recipes')
router.register('ingredients', views.IngredientViewSet, basename='ingredients')
router.register('tags', views.TagViewSet, basename='tags')
router.register(
    r'users/(?P<user_id>\d+)/subscribe', views.SubscribeViewSet,
    basename='subscribe')
router.register(
    r'recipes/(?P<recipe_id>\d+)/favorite', views.FavoriteRecipeViewSet,
    basename='favorite')
router.register(
    r'recipes/(?P<recipe_id>\d+)/shopping_cart', views.ShoppingCartViewSet,
    basename='shoppingcart')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
