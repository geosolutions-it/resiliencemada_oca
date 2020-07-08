### To integrate OCA application inside a geonode-project (3.x), follow the steps below

- Copy the OCA app in one of the paths within the geonode directory
- Add the oca app in geonodes installed apps as shown below
```
INSTALLED_APPS += ([... other_apps], 'your-app-directory.oca')
```
