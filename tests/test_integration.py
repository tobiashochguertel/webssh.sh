"""Integration tests for wshcopy"""
import pytest
import subprocess
import sys
import os


class TestIntegration:
    """Integration tests for the wshcopy command"""
    
    def test_wshcopy_echo_simple(self):
        """Test piping simple text to wshcopy"""
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy'],
            input=b'Hello Integration\n',
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        assert result.returncode == 0
        assert b'\x1b]52;c;' in result.stdout
        assert b'SGVsbG8gSW50ZWdyYXRpb24=' in result.stdout  # Base64 of "Hello Integration"
    
    def test_wshcopy_version(self):
        """Test version flag"""
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy', '--version'],
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        assert result.returncode == 0
        assert b'webssh-sh' in result.stdout
    
    def test_wshcopy_empty_input(self):
        """Test with empty input"""
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy'],
            input=b'',
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        assert result.returncode == 0
        assert result.stdout == b''
    
    def test_wshcopy_multiline(self):
        """Test with multiline input"""
        test_input = b'Line 1\nLine 2\nLine 3\n'
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy'],
            input=test_input,
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        assert result.returncode == 0
        assert b'\x1b]52;c;' in result.stdout
    
    def test_wshcopy_terminal_flag_tmux(self):
        """Test with tmux terminal flag"""
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy', '-t', 'tmux'],
            input=b'Test\n',
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        assert result.returncode == 0
        assert b'\x1bPtmux;\x1b' in result.stdout
    
    def test_wshcopy_terminal_flag_screen(self):
        """Test with screen terminal flag"""
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy', '-t', 'screen'],
            input=b'Test\n',
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        assert result.returncode == 0
        assert b'\x1bP' in result.stdout
