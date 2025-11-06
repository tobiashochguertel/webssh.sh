"""Unit tests for wshcopy module"""
import pytest
import sys
import os
from io import StringIO
from unittest.mock import patch, MagicMock
from wsh import wshcopy


class TestReadStdin:
    """Test read_stdin functionality"""
    
    def test_read_stdin_simple_text(self):
        """Test reading simple text from stdin"""
        test_input = "Hello World\n"
        with patch('sys.stdin', StringIO(test_input)):
            result = wshcopy.read_stdin()
            assert result == "Hello World"
    
    def test_read_stdin_multiline(self):
        """Test reading multiple lines from stdin"""
        test_input = "Line 1\nLine 2\nLine 3\n"
        with patch('sys.stdin', StringIO(test_input)):
            result = wshcopy.read_stdin()
            assert result == "Line 1\nLine 2\nLine 3"
    
    def test_read_stdin_empty(self):
        """Test reading empty stdin"""
        test_input = ""
        with patch('sys.stdin', StringIO(test_input)):
            result = wshcopy.read_stdin()
            assert result == ""
    
    def test_read_stdin_keyboard_interrupt(self):
        """Test handling KeyboardInterrupt"""
        with patch('sys.stdin', MagicMock(side_effect=KeyboardInterrupt)):
            result = wshcopy.read_stdin()
            assert result == ""


class TestTerminalDetection:
    """Test terminal type detection functions"""
    
    def test_is_tmux_with_env(self):
        """Test tmux detection with TMUX environment variable"""
        with patch.dict(os.environ, {'TMUX': '/tmp/tmux-1000/default,1234,0'}):
            wshcopy.terminal = "auto"
            assert wshcopy.is_tmux() is True
    
    def test_is_tmux_without_env(self):
        """Test tmux detection without TMUX environment variable"""
        with patch.dict(os.environ, {}, clear=True):
            wshcopy.terminal = "auto"
            assert wshcopy.is_tmux() is False
    
    def test_is_tmux_forced(self):
        """Test forced tmux terminal type"""
        wshcopy.terminal = "tmux"
        assert wshcopy.is_tmux() is True
    
    def test_is_screen_with_env(self):
        """Test screen detection with TERM environment variable"""
        with patch.dict(os.environ, {'TERM': 'screen'}, clear=True):
            wshcopy.terminal = "auto"
            assert wshcopy.is_screen() is True
    
    def test_is_screen_without_env(self):
        """Test screen detection without screen environment"""
        with patch.dict(os.environ, {'TERM': 'xterm'}, clear=True):
            wshcopy.terminal = "auto"
            assert wshcopy.is_screen() is False
    
    def test_is_screen_forced(self):
        """Test forced screen terminal type"""
        wshcopy.terminal = "screen"
        assert wshcopy.is_screen() is True
    
    def test_is_screen_in_tmux(self):
        """Test that screen is not detected when in tmux"""
        with patch.dict(os.environ, {'TERM': 'screen', 'TMUX': '/tmp/tmux'}):
            wshcopy.terminal = "auto"
            assert wshcopy.is_screen() is False


class TestOSC52Sequence:
    """Test OSC52 sequence generation"""
    
    def test_write_stdout(self, capsys):
        """Test writing to stdout"""
        wshcopy.write_stdout("test")
        captured = capsys.readouterr()
        assert captured.out == "test"
    
    def test_write_osc52_sequence_simple(self, capsys):
        """Test OSC52 sequence for simple text"""
        wshcopy.terminal = "auto"
        with patch.dict(os.environ, {}, clear=True):
            wshcopy.write_osc52_sequence("Hello")
            captured = capsys.readouterr()
            # Base64 of "Hello" is "SGVsbG8="
            assert "\x1b]52;c;" in captured.out
            assert "SGVsbG8=" in captured.out
            assert "\x07" in captured.out
    
    def test_write_osc52_sequence_tmux(self, capsys):
        """Test OSC52 sequence with tmux wrapping"""
        wshcopy.terminal = "tmux"
        wshcopy.write_osc52_sequence("Test")
        captured = capsys.readouterr()
        assert "\x1bPtmux;\x1b" in captured.out
        assert "\x1b\\" in captured.out
    
    def test_write_osc52_sequence_screen(self, capsys):
        """Test OSC52 sequence with screen wrapping"""
        wshcopy.terminal = "screen"
        wshcopy.write_osc52_sequence("Test")
        captured = capsys.readouterr()
        assert "\x1bP" in captured.out
        assert "\x1b\x5c" in captured.out


class TestCLI:
    """Test CLI functionality"""
    
    def test_cli_with_input(self, capsys):
        """Test CLI with text input"""
        test_input = "Hello World\n"
        test_args = ['-t', 'auto']
        
        with patch('sys.stdin', StringIO(test_input)):
            with patch.dict(os.environ, {}, clear=True):
                with patch('sys.argv', ['wshcopy'] + test_args):
                    wshcopy.cli()
        
        captured = capsys.readouterr()
        assert "\x1b]52;c;" in captured.out
    
    def test_cli_version(self, capsys):
        """Test CLI version flag"""
        test_args = ['--version']
        
        with patch('sys.argv', ['wshcopy'] + test_args):
            with pytest.raises(SystemExit) as exc_info:
                wshcopy.cli()
        
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "webssh-sh" in captured.out
    
    def test_cli_empty_input(self):
        """Test CLI with empty input"""
        test_input = ""
        test_args = []
        
        with patch('sys.stdin', StringIO(test_input)):
            with patch('sys.argv', ['wshcopy'] + test_args):
                with pytest.raises(SystemExit) as exc_info:
                    wshcopy.cli()
        
        assert exc_info.value.code == 0
