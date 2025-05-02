import cv2
import numpy as np

# โหลดภาพ
image = cv2.imread('TEST_IMG.png')

# ตรวจสอบว่าไฟล์ภาพถูกโหลดหรือไม่
if image is None:
    print("Error loading image. Please check the file path.")
    exit()

# แปลงภาพเป็นขาวดำ (Grayscale)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# แปลงภาพ grayscale กลับเป็นภาพ 3 ช่องสี
gray_three_channel = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# ปรับสีให้เป็น 3 สี (ใช้ค่าคงที่สำหรับแต่ละช่องสี)
red_channel = gray_three_channel.copy()
green_channel = gray_three_channel.copy()
blue_channel = gray_three_channel.copy()

# ปรับสีให้เป็นสีแดง (Red)
red_channel[:, :, 1] = 0  # กำหนดให้ช่องสีเขียวเป็น 0
red_channel[:, :, 2] = 0  # กำหนดให้ช่องสีน้ำเงินเป็น 0

# ปรับสีให้เป็นสีเขียว (Green)
green_channel[:, :, 0] = 0  # กำหนดให้ช่องสีแดงเป็น 0
green_channel[:, :, 2] = 0  # กำหนดให้ช่องสีน้ำเงินเป็น 0

# ปรับสีให้เป็นสีน้ำเงิน (Blue)
blue_channel[:, :, 0] = 0  # กำหนดให้ช่องสีแดงเป็น 0
blue_channel[:, :, 1] = 0  # กำหนดให้ช่องสีเขียวเป็น 0

# แสดงภาพที่มีการปรับเปลี่ยน
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Red Channel Image', red_channel)
cv2.imshow('Green Channel Image', green_channel)
cv2.imshow('Blue Channel Image', blue_channel)

# รอปิดหน้าต่าง
cv2.waitKey(0)
cv2.destroyAllWindows()
