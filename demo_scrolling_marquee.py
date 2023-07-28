"""ILI9341 demo (Scrolling Marquee)."""
from ili9341 import Display, color565
from time import sleep
from sys import implementation


TFT_DC_PIN = const(21)
TFT_CS_PIN = const(5)
TFT_MISO_PIN = const(19)
TFT_MOSI_PIN = const(23)
TFT_CLK_PIN = const(18)
TFT_RST_PIN = const(22)
TFT_T_CS = const(33)


def test():
    """Scrolling Marquee."""
    try:
        # Implementation dependant pin and SPI configuration
        if implementation.name == 'circuitpython':
            import board
            from busio import SPI
            from digitalio import DigitalInOut
            cs_pin = DigitalInOut(board.P0_15)
            dc_pin = DigitalInOut(board.P0_17)
            rst_pin = DigitalInOut(board.P0_20)
            spi = SPI(clock=board.P0_24, MOSI=board.P0_22)
        else:
            from machine import Pin, SPI
            cs_pin = Pin(TFT_CS_PIN)
            dc_pin = Pin(TFT_DC_PIN)
            rst_pin = Pin(TFT_RST_PIN)
            # Baud rate of 40000000 seems about the max
            spi = SPI(2, baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))

        # Create the ILI9341 display:
        display = Display(spi, dc=dc_pin, cs=cs_pin, rst=rst_pin)
        display.clear()

        # Draw non-moving circles
        display.fill_rectangle(0, 0, 239, 99, color565(27, 72, 156))
        display.fill_rectangle(0, 168, 239, 151, color565(220, 27, 72))

        # Load Marquee image
        display.draw_image('images/Rototron128x26.raw', 56, 120, 128, 26)

        # Set up scrolling
        display.set_scroll(top=152, bottom=100)

        spectrum = list(range(152, 221)) + list(reversed(range(152, 220)))
        while True:
            for y in spectrum:
                display.scroll(y)
                sleep(.1)

    except KeyboardInterrupt:
        display.cleanup()


test()
