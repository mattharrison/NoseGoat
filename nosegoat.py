"""
(c) copyright 2011 - matt harrison

Licensed under PSF license
"""
import os
import sys

from nose.plugins import Plugin
from nose.plugins.plugintest import run_buffered as run

GOAT_1 = r"""
 /\\_//\
 \(o o)/____
   \-/      \
    \ ____, /
    //    || 
   ^^     ^^"""

GOAT_2 = r"""
         /\\//\ 
    _____\(oo)/ 
   /     --\/   
   \  ____||    
    ||    ||    
    ^^    ^^"""

class GoatPlugin(Plugin):
    enabled = True
    name = "goat-plugin"

    def options(self, parser, env=os.environ):
        parser.add_option('', '--no-goat',
                          help='do not use the goat', 
                          action='store_true'
                          )

    def configure(self, options, conf):
        self.enabled = not options.no_goat

    def begin(self):
        sys.stderr.write(GOAT_1)

if __name__ == '__main__':
    run(plugins=[GoatPlugin()])
    
