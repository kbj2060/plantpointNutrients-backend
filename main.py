from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


#########################
# 필요한 정보
# 1. 단계별 A 양액이 들어가는 양
# 2. 단계별 B 양액이 들어가는 양
# 3. 물이 들어가는 양
# 4. 총 기간
# 5. 단계별 기간
# 6. 식물에 양액이 들어가는 총 단계
# 기계
# 1. 솔레노이드 밸브 5ea
# 2. 물 공급용 워터펌프
# 3. 스프레이용 워터펌프
# 4. 양액펌프 2ea
# 센서
# 1. 유량센서
# 2. 온도센서
#########################

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

