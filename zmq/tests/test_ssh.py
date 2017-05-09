import sys

from pytest import mark
from zmq.ssh.tunnel import select_random_ports

@mark.skipif(sys.platform.startswith('win'), reason='Hangs on Windows')
def test_random_ports():
    for i in range(4096):
        ports = select_random_ports(10)
        assert len(ports) == 10
        for p in ports:
            assert ports.count(p) == 1
