po_dir = join_paths(meson.source_root(), 'po')

i18n.merge_file('gsettings-schemas',
  input: 'org.gnome.mousetweaks.gschema.xml.in',
  output: 'org.gnome.mousetweaks.gschema.xml',
  install: true,
  install_dir: schemadir,
  po_dir: po_dir)

install_data('mousetweaks.ui',
  install_dir: join_paths(datadir, 'mousetweaks'))

install_data('mousetweaks.convert',
  install_dir: join_paths(datadir, 'GConf', 'gsettings'))
