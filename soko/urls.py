from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSet,CommentViewSet,ProductViewSet,OrderViewSet,LocationViewSet,ReplyViewSet

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'location', LocationViewSet)
router.register(r'reply', ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]