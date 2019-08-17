""" This context file helps to specify an explicit path notification so that
individual test functions can correctly import the app module as follows:

    from .context import sample

Doing so allows us to test app functionality without having the pip install
the module each time.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import flappy
