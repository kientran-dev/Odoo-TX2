# -*- coding: utf-8 -*-
{
    'name': "Quanlybanhang",

    'summary': """
        Phần mềm quản lý bán hàng trên Odoo""",

    'description': """
       Phần mềm bán hàng - Hệ quản trị daonh nghiệp điện tử ERP
    """,

    'author': "Tran Trung Kien",
    'website': "http://www.banhang.com.vn/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hệ thống quản lý bán hànd trên Odoo',
    'version': '0.1',

    #Them license
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report.xml',
        'report/report_sanpham.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
