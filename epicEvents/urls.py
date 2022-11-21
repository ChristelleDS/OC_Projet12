from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from authentication.views import CreateUserAPIView
from clients.views import ClientViewset
from contracts.views import ContractViewset
from events.views import EventViewset
from django.contrib.auth import views as auth_views


client_router = routers.SimpleRouter()
client_router.register(r'clients', ClientViewset, basename='clients')
# generates:
# /clients/
# /clients/{pk}/

contract_router = routers.NestedSimpleRouter(client_router, r'clients', lookup='client')
contract_router.register(r'contracts', ContractViewset, basename='contracts')
# generates:
# /clients/{client_pk}/contracts/
# clients/{client_pk}/contracts/{pk}/

event_router = routers.NestedSimpleRouter(contract_router, r'contracts', lookup='contract')
event_router.register(r'events', EventViewset, basename='events')
# generates:
# /clients/{client_pk}/contracts/{contract_pk}/events/
# /clients/{client_pk}/contracts/{contract_pk}/events/{pk}/

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user-token/', obtain_auth_token, name="user-token"),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/createUser/', CreateUserAPIView.as_view(), name='createUser'),
    path(r'api/', include(client_router.urls)),
    path(r'api/', include(contract_router.urls)),
    path(r'api/', include(event_router.urls)),

    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
