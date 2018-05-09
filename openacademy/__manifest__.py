{
    'name': "openacademy",
    'version': '1.0',
    'depends': ['base'],
    'author': "Nadal",
    'category': 'Category',
    'description': """
                    MODULE FROM TRAINING.
                   """,
    # data files always loaded at installation
    'data': [
        "views/courses_menu.xml",
        "views/course_views.xml",
        "views/sessions_menu.xml",
        "views/session_views.xml",
        "views/partner_menu.xml",
        "views/partner_views.xml",
        "views/wizard_view.xml"
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        "views/demo_data.xml"
    ],
    'auto_install': False  # If module and all its dependencies have to be installed automatically
}
