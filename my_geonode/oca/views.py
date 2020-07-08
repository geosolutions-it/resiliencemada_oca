import os
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'site_index.html'

    def get_context_data(self):
        f= settings.STATIC_ROOT+'/oca'
        fokontany= os.listdir(f+'/fokontany')
        fkt=[]
        for fok in fokontany:
            fkt.append(os.path.splitext(fok)[0])
            
        bati= os.listdir(f+'/bati')
        eau= os.listdir(f+'/eau')
        route= os.listdir(f+'/route')

        return {
            'fkt': fkt, 'f': f, 'bati': bati, 'eau': eau, 'route': route
        }
