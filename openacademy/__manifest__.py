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
        "views/course_views.xml"
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        "views/demo_data.xml"
    ],
    'auto_install': False  # If module and all its dependencies have to be installed automatically
}
