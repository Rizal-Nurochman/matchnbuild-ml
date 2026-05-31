from sqlalchemy import create_engine, text
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def get_design_items(category: str = None):
  query = "SELECT * FROM design_items"
  params = {}

  if category:
    query += " WHERE category = :category"
    params["category"] = category

  with engine.connect() as conn:
    result = conn.execute(text(query), params)
    columns = result.keys()
    return [dict(zip(columns, row)) for row in result.fetchall()]