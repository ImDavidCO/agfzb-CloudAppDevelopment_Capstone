from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Ruta para la vista about
    path(route='about/', view=views.about, name='about'),

    # Ruta para la vista contact_us
    path(route='contact_us/', view=views.contact_us, name='contact_us'),

    # Ruta para el inicio de sesión
    path(route='login/', view=LoginView.as_view(template_name='djangoapp/login.html'), name='login'),

    # Ruta para cerrar sesión
    path(route='logout/', view=LogoutView.as_view(), name='logout'),

    # Ruta para el registro
    path(route='registration/', view=views.registration, name='registration'),

    path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),

    # Ruta para las revisiones de concesionarios (comentadas por ahora)
    # path(route='dealer/<int:dealer_id>/', view=views.dealer_reviews, name='dealer_reviews'),

    # Ruta para agregar una revisión (comentada por ahora)
    # path(route='add_review/', view=views.add_review, name='add_review'),

    # Ruta para la vista index (get_dealerships)
    path(route='', view=views.get_dealerships, name='index'),

    # Ruta de administrador
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
