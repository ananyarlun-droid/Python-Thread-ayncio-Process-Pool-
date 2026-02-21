# 6810110396 อนัญญา ลุ่นเซียะ
# Python-Thread-ayncio-Process-Pool-
ทดลองเขียนโค้ด Thread asyncio หรือ Process Pool ด้วยภาษา Python

## 1. Thread
ไฟล์: thread_download.py  
จำลองการดาวน์โหลดหลายไฟล์พร้อมกันด้วย threading  
เหมาะกับงาน I/O

---

## 2. asyncio
ไฟล์: asyncio_tasks.py  
ใช้ async/await และ asyncio.gather เพื่อรันหลาย task พร้อมกัน  
เหมาะกับงาน network และงานที่ต้องรอ

---

## 3. Process Pool
ไฟล์: process_pool_prime.py  
ใช้ ProcessPoolExecutor เพื่อคำนวณ prime number  
เหมาะกับงาน CPU-heavy

---  
