import {{cookiecutter.module_name}}

def all():
    import importlib as il

    # Reload package
    il.reload({{cookiecutter.module_name}})

    # Reload operators subpackage
    il.reload({{cookiecutter.module_name}}.operators)

    # Reload panels subpackage
    il.reload({{cookiecutter.module_name}}.panels)

    print('{{cookiecutter.module_name}}: Reload finished.')
