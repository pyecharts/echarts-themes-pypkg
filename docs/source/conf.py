# -*- coding: utf-8 -*-
DESCRIPTION = (
    'packages echarts vintage, macarons, infographic, shine, roma themes' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'echarts-themes-pypkg'
copyright = u'2018 pyecharts dev team'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'echarts-themes-pypkgdoc'
latex_elements = {}
latex_documents = [
    ('index', 'echarts-themes-pypkg.tex',
     'echarts-themes-pypkg Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'echarts-themes-pypkg',
     'echarts-themes-pypkg Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'echarts-themes-pypkg',
     'echarts-themes-pypkg Documentation',
     'pyecharts dev team', 'echarts-themes-pypkg',
     DESCRIPTION,
     'Miscellaneous'),
]
