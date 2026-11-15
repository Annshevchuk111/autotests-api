from pydantic import BaseModel,HttpUrl, Field
from tools.faker import fake

class CreateFileRequestSchema(BaseModel):
    filename: str = Field(default_factory=lambda:f'{fake.uuid4()}.png')
    directory: str = Field(default='tests')
    upload_file: str

class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileResponseSchema(BaseModel):
    file: FileSchema