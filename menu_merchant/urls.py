from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (
    KeywordViewSet,
    HashtagViewSet,
    CategoryViewSet,
    MerchantViewSet,
    PromotionViewSet,
    ProductViewSet,
    ServiceViewSet,
    CollectionViewSet
)


router = SimpleRouter()
router.register('keywords', KeywordViewSet)
router.register('hashtags', HashtagViewSet)
router.register('categories', CategoryViewSet)
router.register('merchants', MerchantViewSet)
router.register('promotions', PromotionViewSet)
router.register('products', ProductViewSet)
router.register('services', ServiceViewSet)
router.register('collections', CollectionViewSet)


urlpatterns = router.urls
