bl_info = {
    'name': '{{cookiecutter.addon_name}}',
    'author': '{{cookiecutter.author}}',
    'version': ({{cookiecutter.version.split('.')|join(', ')}}),
    'blender': ({{cookiecutter.blender_version.split('.')|join(', ')}}),
    'location': '',
    'description': '{{cookiecutter.description}}',
    'warning': '',
    'wiki_url': '',
    'support': 'COMMUNITY',
    'category': '{{cookiecutter.category}}'}

__version__ = '.'.join(map(str, bl_info['version']))


# Handle Reload Scripts
if 'reload' in locals():
    import importlib as il
    il.reload(reload)
    reload.all()

import {{cookiecutter.module_name}}.reload as reload


def register():
    from . import patch
    patch.add_local_modules_to_path()

    from {{cookiecutter.module_name}} import operators
    from {{cookiecutter.module_name}} import panels

    operators.register()
    panels.register()


def unregister():
    from {{cookiecutter.module_name}} import operators
    from {{cookiecutter.module_name}} import panels

    operators.unregister()
    panels.unregister()


if __name__ == '__main__':
    register()
