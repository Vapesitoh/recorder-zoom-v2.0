import runpy
import sys
from unittest.mock import patch
import pytest

import focusrecorder
import focusrecorder.main

def test_script_execution():
    with patch.object(focusrecorder.main, "run") as mock_run:
        with patch.object(sys, "argv", ["__main__.py"]):
            runpy.run_module("focusrecorder.__main__", run_name="__main__")
            mock_run.assert_called_once()

def test_main_block():
    import types
    import runpy
    from unittest.mock import patch
    import focusrecorder.main as main_module
    
    with patch('focusrecorder.main.run') as mock_run:
        saved_name = main_module.__name__
        try:
            main_module.__name__ = '__main__'
            main_module.run()
        finally:
            main_module.__name__ = saved_name
        mock_run.assert_called_once()

def test_dunder_main_block():
    import runpy
    from unittest.mock import patch
    with patch('focusrecorder.main.run') as mock_run:
        try:
            runpy.run_module("focusrecorder.__main__", run_name="__main__")
        except Exception:
            pass

def test_dunder_main_import():
    import focusrecorder.__main__
