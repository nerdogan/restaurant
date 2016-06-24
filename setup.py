__author__ = 'NAMIK'
from distutils.core import setup
import py2exe,sys,os
sys.argv.append('py2exe')

setup(
    name = 'NENrest',
    description = 'Restaurant Automotion',
    version = '1.6.2',
	windows=[{ 'script':'masa.py','icon_resources': [(0, 'nenra.ico')] }],
	options={
    'py2exe': {
    'packages' : ['PyQt4','adodbapi','reportlab','PIL.Image','PIL.PdfImagePlugin',
    'reportlab.graphics.charts',
    'reportlab.graphics.samples',
    'reportlab.graphics.widgets',
    'reportlab.graphics.barcode',
    'reportlab.graphics',
    'reportlab.lib',
    'reportlab.pdfbase',
    'reportlab.pdfgen',
    'reportlab.platypus'],
    'includes':['sip','MySQLdb'],
    'dll_excludes': ['msvcp90.dll','msvcr90.dll'],
    'bundle_files': 1
    }
    },
data_files = [ 'C:\\Python27\\tcl\\tcl8.5\\init.tcl',
            ('phonon_backend',  [ r'C:\Python27\Lib\site-packages\PyQt4\plugins\phonon_backend\phonon_ds94.dll' ]),
                        ]
    )


