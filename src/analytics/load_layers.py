import os
from django.contrib.gis.utils import LayerMapping
from .models import Oblast

oblasti_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'hasc_1' : 'HASC_1',
    'ccn_1' : 'CCN_1',
    'cca_1' : 'CCA_1',
    'type_1' : 'TYPE_1',
    'engtype_1' : 'ENGTYPE_1',
    'nl_name_1' : 'NL_NAME_1',
    'varname_1' : 'VARNAME_1',
    'geom' : 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/SRB_adm1.shp'))
def run(verbose=True):
    lm = LayerMapping(Oblast, county_shp, oblasti_mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)

