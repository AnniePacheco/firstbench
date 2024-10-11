from threading import Lock
from backend.schemas import DocsPathsCreateSchema
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from common.paths import chroma_db_path
from pathlib import Path
import os
from google.cloud import documentai
from google.api_core.client_options import ClientOptions


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ocrnotes-438222-a12036ccd815.json"

class OcrIndexingManager:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(OcrIndexingManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            with self._lock:
                if not hasattr(self, '_initialized'):
                    self._initialized = True
                    self.project_id = os.environ.get('PROJECT_ID')
                    self.location = os.environ.get('LOCATION')
                    self.processor_id = os.environ.get('PROCESSOR_ID')
                    self.endpoint = os.environ.get('ENDPOINT')
                    print("parameters", self.project_id, self.location, self.processor_id, self.endpoint) 

    async def extract_text(self, channel_id: str, docs_paths_data: DocsPathsCreateSchema) -> str:        
        try:
            mime_type = 'application/pdf'
            client = documentai.DocumentProcessorServiceClient(
                client_options=ClientOptions(api_endpoint=self.endpoint))
            name =  client.processor_path(self.project_id, self.location, self.processor_id)
            for path in docs_paths_data["docs_paths"]:
                print(path)
                with open(path, "rb") as image:
                    image_content = image.read()
                raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
                
                request = documentai.ProcessRequest(
                    name=name,
                    raw_document=raw_document)
                response = client.process_document(request=request)
                document = response.document
                print(document.text)
                return document.text
        except Exception as e:
            print("An error occurred while extracting text from the document", e)
            return None
    