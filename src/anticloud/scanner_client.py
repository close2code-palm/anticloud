import clamd


def make_scanner(host: str, port: int) -> clamd.ClamdNetworkSocket:
    return clamd.ClamdNetworkSocket(host, port)