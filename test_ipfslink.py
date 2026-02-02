# test_ipfslink.py
"""
Tests for IPFSLink module.
"""

import unittest
from ipfslink import IPFSLink

class TestIPFSLink(unittest.TestCase):
    """Test cases for IPFSLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IPFSLink()
        self.assertIsInstance(instance, IPFSLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IPFSLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
