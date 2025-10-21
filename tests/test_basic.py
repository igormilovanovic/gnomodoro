"""
Basic tests for Gnomodoro application.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import gnomodoro


def test_version():
    """Test that the version is defined."""
    assert hasattr(gnomodoro, '__version__')
    assert gnomodoro.__version__ == "0.1.0"


def test_author():
    """Test that the author is defined."""
    assert hasattr(gnomodoro, '__author__')
    assert gnomodoro.__author__ == "Igor Milovanovic"


def test_license():
    """Test that the license is defined."""
    assert hasattr(gnomodoro, '__license__')
    assert gnomodoro.__license__ == "MIT"
