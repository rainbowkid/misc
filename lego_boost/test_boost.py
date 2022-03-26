
from pylgbst.hub import MoveHub, COLOR_NONE, COLOR_BLACK, COLORS, COLOR_CYAN, COLOR_BLUE, COLOR_RED, COLOR_YELLOW, COLOR_WHITE
from pylgbst import get_connection_auto
from pylgbst.peripherals import EncodedMotor

import time

mac = "00:16:53:A1:7C:B0"
con = get_connection_auto(hub_mac=mac)
hub = MoveHub(con)


BASE_SPEED = 1.0

hub.motor_AB.angled(290, BASE_SPEED, -BASE_SPEED, end_state=EncodedMotor.END_STATE_FLOAT)
time.sleep(1)
hub.motor_AB.stop()


def print_color(color, distance=-1):
    print(f"Color {COLORS[color]} at a distance of {distance}")

    
hub.vision_sensor.subscribe(print_color)


