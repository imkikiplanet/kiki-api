from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 模擬資料庫
items = {}

# 資料模型
class Item(BaseModel):
    name: str
    description: str = None
    price: float

# GET: 查詢所有項目
@app.get("/gggg")
def gggg():
    return {}


# GET: 查詢所有項目
@app.get("/items")
def get_items():
    return items

# GET: 根據 ID 查詢單一項目
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# POST: 新增一個項目
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item

# PUT: 更新一個項目
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

# DELETE: 刪除一個項目
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}


