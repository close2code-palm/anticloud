from io import BytesIO

import clamd


class FileScanner:
    def __init__(self, clamav_client: clamd.ClamdNetworkSocket):
        self.clamd = clamav_client

    def scan_io(self, data: bytes) -> str | None:
        result = self.clamd.instream(BytesIO(data))
        status, reason = list(result.values())[0]
        if status == "OK":
            return None
        return reason



