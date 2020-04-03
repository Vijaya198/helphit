from django.urls import path
#from path.to.view import Custom404
from . import views
handler404 = 'account_login.views.handler404'
handler500 = 'account_login.views.handler500'
handler403 = 'account_login.views.handler403'
urlpatterns = [


    path('accountinfo', views.accountinfo, name='accountinfo'),
path('editaccountone', views.edit_account1, name='edit_account1'),
path('editaccounttwo', views.edit_account2, name='edit_account2'),
path('editaccountthree', views.edit_account3, name='edit_account3'),
path('editaccountcontact', views.edit_account_contact, name='edit_account_contact'),
path('account_mail', views.account_mail, name='account_mail'),
    path('vendors', views.vendors, name='vendors'),
    path('valid_company_nick_name', views.valid_company_nick_name, name='valid_company_nick_name'),
path('valid_entity_locality', views.valid_entity_locality, name='valid_entity_locality'),
    path('addVendor', views.add_vendor, name='add_vendor'),
    path('vendorRegister',views.vendor_register,name='vendor_register'),
    path('editVendorDetails', views.edit_vendor_details, name='edit_vendor_details'),
path('editcontactaccount', views.edit_contactaccount, name='edit_contactaccount'),
path('edit_account1info', views.edit_account1info, name='edit_account1info'),
path('edit_account2info', views.edit_account2info, name='edit_account2info'),
path('edit_account3info', views.edit_account3info, name='edit_account3info'),
path('edit_account_mail', views.edit_account_mail, name='edit_account_mail'),
    path('updateVendor',views.updateVendor, name='updateVendor'),
    path('deleteVendorDetails', views.delete_vendor_details, name='delete_vendor_details'),
    path('tableInfo',views.table_info, name='table_info'),
    path('traders', views.traders, name='traders'),
    path('viewmore/<str:id>',views.viewmore, name="viewmore"),
    path('confirm', views.confirm, name='confirm'),


]