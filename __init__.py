import os
from os.path import join as _join
from os.path import split as _split

from subprocess import Popen, PIPE, STDOUT

from wepppy.all_your_base.geo import GeoTransformer


_thisdir = os.path.dirname(__file__)

_proj4 = open(_join(_thisdir, 'proj4')).read()
_shp = _join(_thisdir, 'NA_CEC_Eco_Level3.shp')
_gt = GeoTransformer(src_epsg=4326, dst_proj4=_proj4)


def _float_try_parse(v):
    try:
        v = float(v)
    except:
        pass
    return v


def identify(lng, lat):
    global _gt
    x, y = _gt.transform(lng, lat)
    x, y = str(x), str(y)

    cmd = ['ogrinfo', _shp, '-ro', '-al', '-geom=NO', '-spat', x, y, x, y] 
    p = Popen(cmd, bufsize=0, stdin=PIPE, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    res, _ = p.communicate()

    d = {}
    key = None
    for l in res.split('\n'):
        l = l.strip()
        if l == '':
            key = None

        if l.startswith('OGRFeature'):
            key = l.split(':')[-1]
            d[key] = {}

        else:
            if key:
                _k, _v = l.split(' = ')
                d[key][_k] = _float_try_parse(_v)

    return d
        

if __name__ == "__main__":
    d = identify(-121.399334971544,40.5648967867666)
    print(d)
