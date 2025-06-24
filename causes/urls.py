from django.urls import path
from .views import CauseListCreateView, CauseRetrieveUpdateDestroyView, ContributeListCreateView



urlpatterns = [
    path('causes/', CauseListCreateView.as_view(), name='cause-list-create'),
    path('causes/<int:pk>/', CauseRetrieveUpdateDestroyView.as_view(), name='cause-detail'),
    path('causes/<int:id>/contribute/', ContributeListCreateView.as_view(), name='contribute-list-create'),
]