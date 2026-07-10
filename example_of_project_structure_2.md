src 
 api
 models - модели бд
  books.py
 schemas - схемы из pydantic
  books.py
 api - ручки
  books.py
  dependencies.py
  router.py - from src.api.books import router as books_router main_router = APIRouter() main_router.include_router(books_router)
 main.py - должен быть очень кратким
 database.py
