from django.urls import path
from interface_app import views


urlpatterns = [
    # guest system interface:
    # ex : /intereface/case_manage/
    # 用例管理
    path('case_manage/', views.case_manage),
    path('add_case/', views.add_case),
    path("api_debug/",views.api_debug),
    path("save_case/",views.save_case),
    path('get_porject_list', views.get_project_list),
    path('search_case_name/', views.search_case_name),
    path('debug_case/<int:cid>/', views.debug_case),
    path('get_case_info/',views.get_case_info),
]