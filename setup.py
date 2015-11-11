__author__ = 'NAMIK'
from distutils.core import setup
import py2exe,sys,os
sys.argv.append('py2exe')

setup(
    name = 'NENrest',
    description = 'Restaurant Automotion',
    version = '1.3.1',
	windows=[{ 'script':'barcode.py','icon_resources': [(0, 'nenra.ico')] }],
	options={
    'py2exe': {
    'packages' : ['PyQt4','adodbapi','reportlab',
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
    'dll_excludes': [''],
    'bundle_files': 1
    }
    },
data_files = [
            ('phonon_backend',  [ r'C:\Python27\Lib\site-packages\PyQt4\plugins\phonon_backend\phonon_ds94.dll' ]),
            ('datalar', [r'C:\Users\NAMIK\PycharmProjects\restaurant\STOK.pdf']),
            ('imageformats', [ 'C:\\Python27\\Lib\\site-packages\\PyQt4\\plugins\\imageformats\\qico4.dll' ])
            ]
    )


