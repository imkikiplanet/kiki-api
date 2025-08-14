# 使用官方 Python 映像作為基底
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴清單與程式碼
COPY requirements.txt .
COPY index.py .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 開放 Uvicorn 預設的埠
EXPOSE 8000

# 啟動 FastAPI 應用程式
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
