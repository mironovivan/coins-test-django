from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

api_urlpatterns = [
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('payments.urls', 'payments'), namespace='payments')),
]


schema_view = get_swagger_view(title='Test Project API')


urlpatterns = [
    path('api/v1/', include(api_urlpatterns)),
    path('docs/', schema_view),
]
