# 使用官方的 Python 3.11 基礎映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 將需求文件複製到容器中
COPY requirements.txt .

# 安裝所有套件
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update ; apt install curl -y

# 將專案程式碼複製到容器中
COPY . .

# 暴露 5000 Port，讓外面可以連進來
# EXPOSE 8080

# 設定啟動指令
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8080"]
