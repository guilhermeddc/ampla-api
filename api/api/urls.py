from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from core.views import CategoryViewSet, ProductViewSet, ProviderViewSet, ProductCommentsViewSet
from layout.views import IntroProjectViewSet, IntroSlideViewSet, TestimonialsViewSet
from blog.views import BlogCommentsViewSet, PostsViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'products-comments', ProductCommentsViewSet)
router.register(r'projects', IntroProjectViewSet)
router.register(r'intro', IntroSlideViewSet)
router.register(r'testimonials', TestimonialsViewSet)
router.register(r'blog-comments', BlogCommentsViewSet)
router.register(r'posts', PostsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
