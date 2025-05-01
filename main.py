from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome people Juli"}

@app.get ("/items")
async def get_items():
    return {"items": ["item1","item2","item3",]}

@app.post("/items")
async def create_item(name: str):
    return {"message": f"Item {name} created successfully"}