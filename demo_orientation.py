"""ILI9341 demo (orientation)."""
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont


TFT_DC_PIN = const(21)
TFT_CS_PIN = const(5)
TFT_MISO_PIN = const(19)
TFT_MOSI_PIN = const(23)
TFT_CLK_PIN = const(18)
TFT_RST_PIN = const(22)
TFT_T_CS = const(33)


def test():
    """Test code."""
    print('Loading Espresso Dolce font...')
    espresso_dolce = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)
    print('Font loaded.')
    # Baud rate of 40000000 seems about the max
    spi = SPI(2, baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
    
    display = Display(spi, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN),
					  width=240, height=320, rotation=0)
    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 255, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 255, 0), landscape=True)
    sleep(5)
    
    display = Display(spi, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN),
					  width=320, height=240, rotation=90)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 0, 255))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 255, 255), landscape=True)
    sleep(5)
    
    display = Display(spi, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN),
					  width=240, height=320, rotation=180)
    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 0, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 0, 0), landscape=True)
    sleep(5)
    
    display = Display(spi, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN),
					  width=320, height=240, rotation=270)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(225, 0, 128))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 255, 0), landscape=True)
    sleep(5)
    display.cleanup()

test()



