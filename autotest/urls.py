# -*- coding:utf-8 -*-
############################################
#Auther:：Fin
#Version：Autotestplat-V4.0
############################################
from django.urls import path
from . import views, views_index
from . import views_user
from . import views_product
from . import views_interface
from . import views_systemsettings
from . import views_interfacetestplan
from . import views_interfacereport
from . import views_performance
from . import views_apptestcase
from . import views_webtestcase

urlpatterns = [
    path('index/', views_index.indexView, name='index'),
    path('user/', views_user.userView, name='user'),
    path('user/getSearchSelect/', views_user.loadUserRoleSearch),
    path('user/getAddSelect/', views_user.loadAddOptions),
    path('user/getSelect/', views_user.loadOptions),
    path('user/getTableData/', views_user.loadUser),
    path('user/add/', views_user.addUser),
    path('user/mod/', views_user.updateUser),
    path('user/del/', views_user.deleteUser),
    path('login/', views_user.loginView, name='login'),
    path('login/identify/', views_user.login),
    path('login/last/', views_user.lastLogin),
    path('logout/', views_user.logout),
    path('systemsettings/', views_systemsettings.showSystemSettings, name='parasettings'),
    path('systemsettings/getTableData/', views_systemsettings.loadSystemSettings),
    path('systemsettings/add/', views_systemsettings.addSettingsPara),
    path('systemsettings/del/', views_systemsettings.delSettingsPara),
    path('systemsettings/showMod/', views_systemsettings.showModSettingsPara),
    path('systemsettings/mod/', views_systemsettings.saveModSettingsPara),
    path('systemsettings/getSearchSelect/', views_systemsettings.loadParaTypeSearch),
    path('systemsettings/getSelect/', views_systemsettings.loadParaOption),
    path('product/', views_product.productView, name='product'),
    path('product/getTableData/', views_product.loadProduct),
    path('product/add/', views_product.addProduct),
    path('product/mod/', views_product.updateProduct),
    path('product/del/', views_product.deleteProduct),
    path('apitestcase/', views_interface.apiTestcase,name='apitestcase'),
    path('apitestcase/show_add_window/', views_interface.showAddWindow),
    path('apitestcase/add/', views_interface.addInterfaces),
    path('apitestcase/search/', views_interface.searchInterface),
    path('apitestcase/show_edit_interface/<str:edit_id>/<str:action>/', views_interface.showEditInterface),
    path('apitestcase/save_edit_interface/<str:edit_id>/', views_interface.saveEditInterface),
    path('apitestcase/save_copy_interface/<str:edit_id>/', views_interface.saveCopyInterface),
    path('apitestcase/del/', views_interface.delInterface),
    path('apitestcase/send/', views_interface.startInterfaceSend),
    path('apitestcase/show_request_data/', views_interface.showRequestData),
    path('apitestplan/', views_interfacetestplan.interfaceTestplan,name='apitestplan'),
    path('apitestplan/add/', views_interfacetestplan.addTestplan),
    path('apitestplan/show_edit_testplan/', views_interfacetestplan.showEditTestplan),
    path('apitestplan/mod/', views_interfacetestplan.saveEditTestplan),
    path('apitestplan/update/', views_interfacetestplan.updateTestplanInterface),
    path('apitestplan/del_row/', views_interfacetestplan.delRow),
    path('apitestplan/del_row_edit/', views_interfacetestplan.delRowEdit),
    path('apitestplan/del/', views_interfacetestplan.delTestplan),
    path('apitestplan/search/', views_interfacetestplan.searchTestplan),
    path('apitestplan/apitestcase/search/', views_interfacetestplan.searchTestplanApiTestcase),
    path('apitestplan/run/', views_interfacetestplan.startInterfaceTestplan),
    path('apitestplan/run/<str:suit_id>/', views_interfacetestplan.runTestplan),
    path('apitestplan/get/<str:suit_id>/', views_interfacetestplan.getProgress),
    path('report/', views_interfacereport.reportView, name='apireport'),
    path('report/getTableData/', views_interfacereport.loadReport),
    path('report/getReportDetail/<str:report_id>/', views_interfacereport.getReportDetail, name='reportdetail'),
    path('report/del/', views_interfacereport.deleteReport),
    path('apiperformance/', views_performance.apiPerformance, name='apiperformance'),
    path('apiperformance/search/', views_performance.searchPerformanceInterface),
    path('apiperformance/generate/', views_performance.generateJmeterFile),
    path('apiperformance/prepare/', views_performance.prepareJmeter),
    path('apiperformance/start/', views_performance.startTestJmeter),
    path('apiperformance/progress/', views_performance.showProgress),
    path('apptestcase/', views_apptestcase.getAppView, name='apptestcase'),
    path('apptestcase/getSearchSelect/', views_apptestcase.loadAppOptions),
    path('apptestcase/getTableData/', views_apptestcase.loadAppTestcaseTable),
    path('apptestcase/addApptestcase/', views_apptestcase.addApptestcase),
    path('apptestcase/delApptestcase/', views_apptestcase.deleteApptestcase),
    path('apptestcase/showModAppTestcase/',views_apptestcase.showModAppTestcase),
    path('apptestcase/modApptestcase/', views_apptestcase.modApptestcase),
    path('apptestcase/showCopyAppTestcase/', views_apptestcase.showCopyAppTestcase),
    path('apptestcase/copyApptestcase/', views_apptestcase.copyApptestcase),
    path('apptestcase/run_apptestcase/<int:app_testcase_code>', views_apptestcase.runApptestcase),
    path('apptestcase/runAllTestcase/', views_apptestcase.runAllTestcase),

    path('webtestcase/', views_webtestcase.getWebView, name='webtestcase'),
    path('webtestcase/getSearchSelect/', views_webtestcase.loadWebOptions),
    path('webtestcase/getTableData/', views_webtestcase.loadWebTestcaseTable),
    path('webtestcase/addWebtestcase/', views_webtestcase.addWebtestcase),
    path('webtestcase/delWebtestcase/', views_webtestcase.deleteWebtestcase),
    path('webtestcase/showModWebTestcase/', views_webtestcase.showModWebTestcase),
    path('webtestcase/modWebtestcase/', views_webtestcase.modWebtestcase),
    path('webtestcase/showCopyWebTestcase/', views_webtestcase.showCopyWebTestcase),
    path('webtestcase/copyWebtestcase/', views_webtestcase.copyWebtestcase),
    path('webtestcase/run_webtestcase/<int:web_testcase_code>', views_webtestcase.runWebtestcase),
    path('webtestcase/runAllTestcase/', views_webtestcase.runAllTestcase),
]