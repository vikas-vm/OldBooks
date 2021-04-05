
from django.contrib import admin
from django.urls import path
from datawork import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="homepage"),
    path('insert/',views.insert,name="insert"),
    path('category/<int:cat_id>',views.category,name="category"),
    path('topic/<int:topic_id>',views.topic,name="topic"),
    path('item/<int:book_id>',views.items,name="item"),
    path('search/',views.search,name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
