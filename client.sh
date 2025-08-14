#!/bin/bash

# 伺服器位置
BASE_URL="http://localhost:8000"

echo "🚀 測試 FastAPI RESTful API"
echo "==========================="

curl -s -X DELETE "$BASE_URL/items/1"

echo "➕ 新增資料 (POST)"
curl -s -X POST "$BASE_URL/items/1" \
-H "Content-Type: application/json" \
-d '{
  "name": "Apple",
  "description": "A juicy red fruit",
  "price": 1.99
}'

echo "📋 查詢所有資料 (GET)"
curl -s -X GET "$BASE_URL/items"

echo "🔍 查詢單筆資料 (GET /items/1)"
curl -s -X GET "$BASE_URL/items/1"

echo "✏️ 更新資料 (PUT)"
curl -s -X PUT "$BASE_URL/items/1" \
-H "Content-Type: application/json" \
-d '{
  "name": "Green Apple",
  "description": "Sour but tasty",
  "price": 2.49
}'

echo "📋 再次查詢所有資料 (GET)"
curl -s -X GET "$BASE_URL/items"

echo "❌ 刪除資料 (DELETE)"
curl -s -X DELETE "$BASE_URL/items/1"

echo "📋 最後檢查資料 (GET)"
curl -s -X GET "$BASE_URL/items"

echo "✅ 測試完成"

