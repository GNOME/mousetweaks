#!/usr/bin/env python3

import os
import subprocess

prefix = os.environ['MESON_INSTALL_PREFIX']
datadir = os.path.join(prefix, 'share')
schemadir = os.path.join(datadir, 'glib-2.0', 'schemas')

if 'DESTDIR' not in os.environ:
    print('Compiling GSettings schemas...')
    subprocess.call(['glib-compile-schemas', schemadir])
