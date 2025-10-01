# Booking Web App (OOP + Streamlit)

ระบบ **จองห้องเรียน / ห้องประชุม** พัฒนาด้วย **Python + Streamlit** โดยเน้นหลักการ **Object-Oriented Programming (OOP)** ครบทั้ง 4 ข้อ (Encapsulation, Abstraction, Inheritance, Polymorphism)

---

## 🔑 สิ่งที่โปรแกรมทำได้

1. สร้างห้องใหม่ (Host)
2. ลบห้อง (Host) — ลบได้เฉพาะเจ้าของห้องและห้องที่ยังไม่ถูกจอง
3. จองห้อง / ยกเลิกการจอง (Booker)
4. ค้นหาห้องตามชื่อ keyword
5. แสดงตารางห้องพร้อมสถานะ
6. ใช้ Streamlit UI แบบ sidebar และ table

---

## ⚡ Feature / Function

| Function                        | ผู้ใช้  | รายละเอียด                                   |
| ------------------------------- | ------- | -------------------------------------------- |
| add_room(room)                  | Host    | เพิ่มห้องใหม่ หากรหัสห้องซ้ำจะล้มเหลว        |
| remove_room(room_id, host_user) | Host    | ลบห้องเฉพาะเจ้าของและยังไม่ถูกจอง            |
| get_all_rooms()                 | ทั้งหมด | ดึงรายชื่อห้องทั้งหมด                        |
| search_rooms(keyword)           | ทั้งหมด | ค้นหาห้องตามชื่อ                             |
| book_room(room_id, booker)      | Booker  | จองห้อง ถ้าห้องว่าง                          |
| cancel_booking(room_id, booker) | Booker  | ยกเลิกการจอง ถ้าเจ้าของการจองตรงกับผู้ยกเลิก |

---

## 🏛 หลักการ OOP ที่ใช้

| Class / Method        | OOP Principle                                     | บรรทัด |
| --------------------- | ------------------------------------------------- | ------ |
| Room                  | Encapsulation                                     | 10–28  |
| User                  | Abstraction                                       | 31–36  |
| HostUser / BookerUser | Inheritance + Polymorphism                        | 39–48  |
| BookingSystem         | Encapsulation + Method-based interface            | 51–83  |
| Streamlit App         | ใช้ OOP objects (`Room`, `User`, `BookingSystem`) | 86–188 |

### 1️⃣ Encapsulation

* `Room` class ใช้ **private attributes** (`__is_booked`, `__booked_by`)
* ใช้ **getter และ method** (`book`, `cancel_booking`) เพื่อเข้าถึงและแก้ไขข้อมูลอย่างปลอดภัย

### 2️⃣ Abstraction

* `User` เป็น **abstract class** พร้อม `abstract method` `role()`
* Subclass ต้อง implement `role()` เอง

### 3️⃣ Inheritance

* `HostUser` และ `BookerUser` **สืบทอดจาก `User`**
* ใช้ `super().__init__()` ใน constructor

### 4️⃣ Polymorphism

* `role()` ใน `HostUser` และ `BookerUser` มี **behavior ต่างกัน**
* สามารถเรียกผ่าน object ของ `User` แล้วได้ผลลัพธ์แตกต่างกัน

---

## 🖥 การติดตั้งและรัน

```bash
# ติดตั้ง dependencies
pip install streamlit pandas

# รันแอป
streamlit run booking_web.py
```

---

## 💡 ตัวอย่างการใช้งาน

1. เปิดแอปแล้วสร้างห้องใหม่ผ่าน Sidebar
2. ดูตารางห้องและสถานะ
3. เลือกห้องแล้วทำการจองหรือยกเลิกการจอง
4. Host สามารถลบห้องที่ยังไม่ถูกจอง

---

## 🎨 UI / UX

* ใช้ sidebar สำหรับ **สร้างห้องและค้นหาห้อง**
* แสดงตารางห้องพร้อมสถานะในหน้า Main
* ใช้ Streamlit columns สำหรับ **จอง / ยกเลิกห้อง** และ **ลบห้อง**
