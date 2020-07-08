### To integrate OCA application inside a geonode-project (3.x), follow the steps below

- Copy the OCA app in one of the paths within the geonode directory
- Add the oca app in geonodes installed apps as shown below
```
INSTALLED_APPS += ([... other_apps], 'your-app-directory.oca')
```

###### Alternatively
- Install the OCA app
```
$ pip install https://github.com/geosolutions-it/resiliencemada_oca/archive/master.zip
```

- Add the oca app in geonodes installed apps as shown below
```
INSTALLED_APPS += ([... other_apps], 'your-app-directory.oca')
```

- Create a route for the OCA index page
```
from django.conf.urls import url, include
from django.views.generic import TemplateView

from geonode.urls import urlpatterns
from oca import HomePage

urlpatterns += [
## include your urls here

]

urlpatterns = [
   url(r'^/?$', HomePage.as_view(), name='home'),
 ] + urlpatterns
```