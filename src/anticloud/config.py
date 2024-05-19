import os


def get_clamav_host_and_port() -> tuple[str, int]:
    host_and_port = os.environ.get('CLAMAV_SERVICE')
    if not host_and_port:
        return "127.0.0.1", 3310
    host, port = host_and_port.split(':')
    return host, int(port)
