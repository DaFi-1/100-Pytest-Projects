import pytest

def x():
    with open('y.c', 'r') as z:
        return z.read()

class TestX:
    def test_x(self, monkeypatch):

        def fekeobj(self):
        class FakeOpen:
            def read():return 'fake'
            def __enter__(self): return self
            def __exit__(*args): pass
        return FakeOpen()

        monkeypatch.setattr('builtins.open', self.fekeobj)
        assert x() == 'fake'



















































