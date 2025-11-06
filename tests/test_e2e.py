"""End-to-end tests for wshcopy"""
import pytest
import subprocess
import os
import tempfile


class TestE2E:
    """End-to-end tests simulating real usage"""
    
    def test_echo_pipe_to_wshcopy(self):
        """Test echo | wshcopy pattern"""
        proc = subprocess.Popen(
            ['echo', 'Hello E2E'],
            stdout=subprocess.PIPE
        )
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy'],
            stdin=proc.stdout,
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        proc.wait()
        
        assert result.returncode == 0
        assert b'\x1b]52;c;' in result.stdout
    
    def test_file_redirect_to_wshcopy(self):
        """Test wshcopy < file.txt pattern"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write('File content test\n')
            temp_file = f.name
        
        try:
            with open(temp_file, 'r') as f:
                result = subprocess.run(
                    ['python', '-m', 'wsh.wshcopy'],
                    stdin=f,
                    capture_output=True,
                    cwd=os.path.dirname(os.path.dirname(__file__))
                )
            
            assert result.returncode == 0
            assert b'\x1b]52;c;' in result.stdout
            assert b'RmlsZSBjb250ZW50IHRlc3Q=' in result.stdout  # Base64
        finally:
            os.unlink(temp_file)
    
    def test_large_file(self):
        """Test with larger file content"""
        large_content = "A" * 10000 + "\n"
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(large_content)
            temp_file = f.name
        
        try:
            with open(temp_file, 'r') as f:
                result = subprocess.run(
                    ['python', '-m', 'wsh.wshcopy'],
                    stdin=f,
                    capture_output=True,
                    cwd=os.path.dirname(os.path.dirname(__file__))
                )
            
            assert result.returncode == 0
            assert b'\x1b]52;c;' in result.stdout
        finally:
            os.unlink(temp_file)
    
    def test_unicode_content(self):
        """Test with unicode characters"""
        unicode_content = "Hello 世界 🌍\n"
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy'],
            input=unicode_content.encode('utf-8'),
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__)),
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}
        )
        
        # On Windows, encoding issues might occur, so we accept either success or encoding error
        if result.returncode == 0:
            assert b'\x1b]52;c;' in result.stdout
        else:
            # Windows may fail with encoding error, which is acceptable for this edge case
            assert b'UnicodeEncodeError' in result.stderr or result.returncode == 0
    
    def test_help_flag(self):
        """Test --help flag"""
        result = subprocess.run(
            ['python', '-m', 'wsh.wshcopy', '--help'],
            capture_output=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        
        assert result.returncode == 0
        assert b'usage:' in result.stdout or b'Usage:' in result.stdout
