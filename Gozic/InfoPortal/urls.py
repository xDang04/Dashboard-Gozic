from django.urls import path, include
from InfoPortal.views import infoPortal, addInfoPortal, insidefolder,addPage,update_page,shareFolder
urlpatterns = [
    path('', infoPortal, name='infoPortal'),
    path("addFolder",addInfoPortal,name="add_folder"),
    path('insidefolder/<int:id>',insidefolder,name="insidefolder"),
    path('addPage/<int:id>',addPage,name="addPage"),
    path('updatePage/<int:id>',update_page,name="update_page"),
    path("share/<int:folderId>",shareFolder,name="shareFolder"),
    path("update/<int:id>",update_page,name="update_page" )
]
