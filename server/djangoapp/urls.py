from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for about view
    path(route='about/', view=views.about, name='about'),

    # path for contact us view
    path(route='contact_us/', view=views.contact_us, name='contact_us'),

    # path for registration
    path(route='login/', view=LoginView.as_view(template_name='djangoapp/login.html'), name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
    path(route='registration/', view=views.registration, name='registration'),

    # path for dealer reviews view
    #path(route='dealer/<int:dealer_id>/', view=views.dealer_reviews, name='dealer_reviews'),

    # path for add a review view
    #path(route='add_review/', view=views.add_review, name='add_review'),

    # path for index view (get_dealerships)
    path('admin/', admin.site.urls),
    path(route='', view=views.get_dealerships, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
