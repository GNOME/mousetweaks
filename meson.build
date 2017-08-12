project('mousetweaks', 'c',
  version: '3.12.0',
  license: 'GPL3+')

datadir = get_option('datadir')
localedir = get_option('localedir')
schemadir = join_paths(datadir, 'glib-2.0', 'schemas')

configinc = include_directories('.')

gnome = import('gnome')
i18n = import('i18n')

gtk = dependency('gtk+-3.0', version: '>= 3.0.0')
x11 = dependency('x11')
xcursor = dependency('xcursor')
xfixes = dependency('xfixes')
xtst = dependency('xtst')

mousetweaks_conf = configuration_data()

mousetweaks_conf.set_quoted('GETTEXT_PACKAGE', 'mousetweaks')
mousetweaks_conf.set_quoted('GNOMELOCALEDIR', localedir)

configure_file(input: 'config.h.meson',
  output: 'config.h',
  configuration: mousetweaks_conf)

subdir('data')
subdir('man')
subdir('pixmaps')
subdir('po')
subdir('src')

meson.add_install_script('meson_post_install.py')
