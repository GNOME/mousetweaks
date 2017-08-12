mousetweaks_enums = gnome.mkenums('mousetweaks-enum-types',
  sources: ['mt-common.h'],
  c_template: 'mt-enum-types.c.template',
  h_template: 'mt-enum-types.h.template',
  install_dir: schemadir)

# https://github.com/mesonbuild/meson/issues/1687
custom_target('mousetweaks-enums',
  input: ['mt-common.h'],
  output: ['org.gnome.mousetweaks.enums.xml'],
  command: [
    'glib-mkenums',
    '--comments', '<!-- @comment@ -->',
    '--fhead', '<schemalist>',
    '--vhead', '  <@type@ id=\'org.gnome.mousetweaks.@EnumName@\'>',
    '--vprod', '    <value nick=\'@valuenick@\' value=\'@valuenum@\'/>',
    '--vtail', '  </@type@>',
    '--ftail', '</schemalist>',
    '@INPUT@'
  ],
  install: true,
  install_dir: schemadir,
  capture: true)

mousetweaks_sources = [
  mousetweaks_enums,
  'mt-main.c',
  'mt-common.c',
  'mt-common.h',
  'mt-pidfile.c',
  'mt-pidfile.h',
  'mt-service.c',
  'mt-service.h',
  'mt-ctw.c',
  'mt-ctw.h',
  'mt-timer.c',
  'mt-timer.h',
  'mt-cursor.c',
  'mt-cursor.h',
  'mt-cursor-manager.c',
  'mt-cursor-manager.h',
  'mt-listener.c',
  'mt-listener.h',
  'mt-sig-handler.c',
  'mt-sig-handler.h',
  'mt-settings.c',
  'mt-settings.h'
]

mousetweaks_c_args = [
  '-DDATADIR="@0@"'.format(join_paths(datadir, 'mousetweaks')),
  '-DHAVE_CONFIG_H=1'
]

mousetweaks = executable('mousetweaks', mousetweaks_sources,
  dependencies: [gtk, x11, xcursor, xfixes, xtst],
  c_args: [mousetweaks_c_args],
  include_directories: [configinc],
  install: true)
