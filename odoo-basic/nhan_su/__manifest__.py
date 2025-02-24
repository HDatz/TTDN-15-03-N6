# -*- coding: utf-8 -*-
{
    'name': "Nhân Sự",

    'summary': """
        Quản lý thông tin nhân viên, bao gồm mã định danh, họ tên, ngày sinh, quê quán, email và số điện thoại.
    """,

    'description': """
        Module Nhân Sự giúp quản lý thông tin cơ bản của nhân viên như mã định danh, họ tên, ngày sinh, quê quán, email, và số điện thoại.
    """,

    'author': "FINT",
    'website': "http://www.fint.com.vn",

    # Categories can be used to filter modules in modules listing
    'category': 'Human Resources',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/nhan_vien_views.xml',  # Đảm bảo đường dẫn đúng
        'security/ir.model.access.csv',  # Nếu có quyền truy cập cần thiết
    ],

    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',  # Nếu bạn có dữ liệu mẫu
    # ],
}
