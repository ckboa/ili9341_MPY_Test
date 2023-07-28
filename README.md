# ili9341_MPY_Test
ทดสอบการใช้บอร์ด PlaySmart กับโค้ดจาก Micropython-ili9341 (https://github.com/rdagger/micropython-ili9341) 

บอร์ด PlaySmart 

![image](https://github.com/ckboa/ili9341_MPY_Test/assets/48851053/27e30f80-3ae6-426c-a8bc-37447fff1245)

การจัดเรียงพินเพื่อรองรับการเชื่อมต่อจอ TFT ขนาด 2.8 นิ้ว 

![image](https://github.com/ckboa/ili9341_MPY_Test/assets/48851053/9ed19ad9-c026-4acf-942c-9e4fbcc6f019)


การกำหนดค่าให้กับไมโครไพทอน 

TFT_DC_PIN = const(21)

TFT_CS_PIN = const(5)

TFT_MISO_PIN = const(19)

TFT_MOSI_PIN = const(23)

TFT_CLK_PIN = const(18)

TFT_RST_PIN = const(22)

การเรียกใช้งานจากเดิมการกำหนดค่าภายใน github เป็น SPI 1 ให้เปลี่ยนเป็น SPI 2 ดังนี้ 

    spi = SPI(2, baudrate=40000000, miso=Pin(TFT_MISO_PIN), mosi=Pin(TFT_MOSI_PIN), sck=Pin(TFT_CLK_PIN))
    display = Display(spi, cs=Pin(TFT_CS_PIN), dc=Pin(TFT_DC_PIN), rst=Pin(TFT_RST_PIN), width=320, height=240)

