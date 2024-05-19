import clamd
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from starlette import status

from config import get_clamav_host_and_port
from file_scan import FileScanner
from scanner_client import make_scanner


def app_factory():
    app = FastAPI()
    scanner_client = make_scanner(*get_clamav_host_and_port())
    scanner = FileScanner(scanner_client)

    @app.post('/')
    async def scan(file: UploadFile):
        buf = await file.read()
        try:
            result = scanner.scan_io(buf)
        except clamd.BufferTooLongError:
            raise HTTPException(status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, "Не удалось просканировать")
        if result:
            return {"Найдено": result}
        return {"status": "Ok"}

    return app


# uvicorn.run(app_factory())
