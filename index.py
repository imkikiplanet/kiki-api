from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime

app = FastAPI()

# 啟用 CORS 政策，讓你的網頁可以呼叫 API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定義接收的資料模型
class ZodiacRequest(BaseModel):
    date: str

# 定義星座的日期區間，加上中文和 emoji
zodiac_signs = {
    '摩羯座 ♑': (1, 20),
    '水瓶座 ♒': (2, 19),
    '雙魚座 ♓': (3, 20),
    '牡羊座 ♈': (4, 20),
    '金牛座 ♉': (5, 20),
    '雙子座 ♊': (6, 21),
    '巨蟹座 ♋': (7, 22),
    '獅子座 ♌': (8, 22),
    '處女座 ♍': (9, 22),
    '天秤座 ♎': (10, 23),
    '天蠍座 ♏': (11, 21),
    '射手座 ♐': (12, 21),
}

@app.post('/get_zodiac')
def get_zodiac_sign(request: ZodiacRequest):
    try:
        birth_date = datetime.datetime.strptime(request.date, '%Y-%m-%d').date()
        month = birth_date.month
        day = birth_date.day

        zodiac = "未知"
        for sign, (start_month, start_day) in zodiac_signs.items():
            if (month == start_month and day >= start_day) or \
               (month == (start_month % 12 + 1) and day < start_day):
                zodiac = sign
                break

        # 修正跨年判斷
        if (month == 12 and day >= 22) or (month == 1 and day <= 19):
            zodiac = '摩羯座 ♑'
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            zodiac = '射手座 ♐'

        return {"zodiac": zodiac}

    except ValueError:
        raise HTTPException(status_code=400, detail="生日日期格式不正確")