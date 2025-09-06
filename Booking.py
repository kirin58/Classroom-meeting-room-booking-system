# booking_web.py
import streamlit as st
import pandas as pd
from abc import ABC, abstractmethod   # สำหรับ Abstraction
 
# ---------------- Models ----------------
class Room:
    def __init__(self, room_id, name, room_type, owner):
        self.room_id = room_id
        self.name = name
        self.room_type = room_type
        self.owner = owner      
        self.__is_booked = False       # Encapsulation
        self.__booked_by = None        # Encapsulation
 
    # Getter & Setter เพื่อเข้าถึงแบบปลอดภัย
    @property
    def is_booked(self):
        return self.__is_booked
 
    @property
    def booked_by(self):
        return self.__booked_by
 
    def book(self, booker):
        if not self.__is_booked:
            self.__is_booked = True
            self.__booked_by = booker
            return True
        return False
 
    def cancel_booking(self, booker):
        if self.__is_booked and self.__booked_by.username == booker.username:
            self.__is_booked = False
            self.__booked_by = None
            return True
        return False
 
 
# Abstraction
class User(ABC):  
    def __init__(self, username):
        self.username = username
 
    @abstractmethod
    def role(self):
        pass
 
 
class HostUser(User):  
    def __init__(self, username):
        super().__init__(username)
 
    def role(self):   # Polymorphism
        return "Host"
 
 
class BookerUser(User):  
    def __init__(self, username):
        super().__init__(username)
 
    def role(self):   # Polymorphism
        return "Booker"
 
 
class BookingSystem:
    def __init__(self):
        self.rooms = []
 
    def add_room(self, room):
        for r in self.rooms:
            if r.room_id == room.room_id:
                return False
        self.rooms.append(room)
        return True
 
    def remove_room(self, room_id, host_user):
        for room in self.rooms:
            if room.room_id == room_id and room.owner.username == host_user.username:
                if room.is_booked:
                    return False
                self.rooms.remove(room)
                return True
        return False
 
    def get_all_rooms(self):
        return self.rooms
 
    def search_rooms(self, keyword):
        return [room for room in self.rooms if keyword.lower() in room.name.lower()]
 
    def book_room(self, room_id, booker):
        for room in self.rooms:
            if room.room_id == room_id:
                return room.book(booker)  # ใช้ encapsulation ผ่าน method ของ Room
        return False
 
    def cancel_booking(self, room_id, booker):
        for room in self.rooms:
            if room.room_id == room_id:
                return room.cancel_booking(booker)  # ใช้ encapsulation
        return False
