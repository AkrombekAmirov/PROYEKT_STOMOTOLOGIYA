from .models import FileChunk, FileRepository
from sqlalchemy.orm.session import Session

chunk_size = 262144
FILE_SIZE = 524288


class FileService:
    def __init__(self, engine):
        self.engine = engine

    def create_file(self, **kwargs):
        session = Session(bind=self.engine)
        result = FileRepository(**kwargs)
        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()
        return result.file_id

    def create_file_chunk(self, image: bytes, file_uuid: str):
        session = Session(bind=self.engine)
        current_chunk = 0
        done_reading = False
        while not done_reading:
            bfr = image[current_chunk * chunk_size: (current_chunk + 1) * chunk_size]
            if not bfr:
                done_reading = True
                break
            bfr = bytearray(bfr)
            result = FileChunk(file_id=file_uuid, chunk=bfr)
            session.add(result)
            session.commit()
            session.refresh(result)
            current_chunk += 1

    # def get_file(self, file_id: str):
    #     session = Session(bind=self.engine)
    #     result = session.query()

