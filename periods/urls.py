from django.conf.urls import include, url
from django.views.generic import RedirectView
from rest_framework import routers

from periods import views as period_views


router = routers.DefaultRouter()
router.register(r'periods', period_views.FlowEventViewSet, base_name='periods')
router.register(r'statistics', period_views.StatisticsViewSet, base_name='statistics')


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='calendar/', permanent=False)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', period_views.ProfileUpdateView.as_view(), name='user_profile'),
    url(r'^accounts/profile/api_info/$', period_views.ApiInfoView.as_view(), name='api_info'),
    url(r'^accounts/profile/regenerate_key/$', period_views.RegenerateKeyView.as_view(),
        name='regenerate_key'),

    url(r'^api/v2/', include(router.urls)),
    url(r'^api/v2/authenticate/$', period_views.ApiAuthenticateView.as_view(), name='authenticate'),
    url(r'^api/v2/aeris/$', period_views.AerisView.as_view(), name='aeris'),
    url(r'^flow_event/$', period_views.FlowEventCreateView.as_view(), name='flow_event_create'),
    url(r'^flow_event/(?P<pk>[0-9]+)/$', period_views.FlowEventUpdateView.as_view(),
        name='flow_event_update'),
    url(r'^flow_events/$', period_views.FlowEventFormSetView.as_view(), name='flow_events'),
    url(r'^calendar/$', period_views.CalendarView.as_view(), name='calendar'),
    url(r'^statistics/$', period_views.StatisticsView.as_view(), name='statistics'),
    url(r'^statistics/cycle_length_frequency/$', period_views.CycleLengthFrequencyView.as_view()),
    url(r'^statistics/cycle_length_history/$', period_views.CycleLengthHistoryView.as_view()),
    url(r'^statistics/qigong_cycles/$', period_views.QigongCycleView.as_view()),
]
