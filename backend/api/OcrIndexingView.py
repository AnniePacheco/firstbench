from starlette.responses import JSONResponse, Response
from backend.managers.OcrIndexingManager import OcrIndexingManager
from backend.pagination import parse_pagination_params
from backend.schemas import DocsPathsCreateSchema


class OcrIndexingView:
    def __init__(self):
        self.ocrm = OcrIndexingManager()   

    async def post(self, resource_id: str, body: DocsPathsCreateSchema):               
        text = await self.ocrm.extract_text(resource_id, body)        
        return JSONResponse(status_code=200, content={"extracted_text": text, "message": "Document processed successfully"})