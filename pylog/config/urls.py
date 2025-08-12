from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config.views import index
from blog.views import post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("posts/", post_list),
    path("posts/<int:post_id>/", post_detail),
]
urlpatterns += static(
    # URL의 접두어가 MEDIA_URL일 때는 정적파일을 돌려준다
    prefix=settings.MEDIA_URL,
    # 돌려줄 디렉터리는 MEDIA_ROOT를 기준으로 한다
    document_root=settings.MEDIA_ROOT,
)
