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



1. Class

มี class ทั้งหมด 5 คลาส

Room

User (abstract base class)

HostUser (extends User)

BookerUser (extends User)

BookingSystem

2. Encapsulation

ตัวแปรภายในแต่ละคลาสถูกกำหนดเป็น private

Room.__is_booked → [บรรทัด 11]

Room.__booked_by → [บรรทัด 12]

ใช้ getter และ method ในการเข้าถึงและแก้ไขค่า

Room.is_booked → [บรรทัด 15]

Room.booked_by → [บรรทัด 18]

Room.book() → [บรรทัด 20–26]

Room.cancel_booking() → [บรรทัด 28–34]

3. Inheritance

HostUser และ BookerUser สืบทอดจาก User → [บรรทัด 39, 46]

ใช้ super().__init__() เพื่อเรียก constructor ของ superclass → [บรรทัด 40, 47]

4. Polymorphism

role() ใน HostUser และ BookerUser มี behavior ต่างกัน → [บรรทัด 41–43, 48]

สามารถเรียกผ่าน object ของ User แล้วได้ผลลัพธ์แตกต่างกัน

5. Abstraction

User เป็น abstract class → [บรรทัด 31–36]

มี abstract method role() ให้ subclass implement → [บรรทัด 34–36]
