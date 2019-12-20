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

def register():
    from . import patch
    patch.add_local_modules_to_path()

    from .operators import register
    register()


def unregister():
    from .operators import unregister
    unregister()


if __name__ == '__main__':
    from .operators import register
    register()
