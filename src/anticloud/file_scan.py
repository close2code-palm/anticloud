import logging
from io import BytesIO

import clamd

from errors import CheckFailed


class FileScanner:
    def __init__(self, clamav_client: clamd.ClamdNetworkSocket):
        self.clamd = clamav_client

    def scan_io(self, data: bytes) -> str | None:
        for i in range(4):
            try:
                result = self.clamd.instream(BytesIO(data))
                break
            except BrokenPipeError:
                logging.error("retry %s", i + 1)
                continue
        else:
            raise CheckFailed
        status, reason = list(result.values())[0]
        if status == "OK":
            return None
        return reason



