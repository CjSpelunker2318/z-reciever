
basic.show_string("RECEIVER")
radio.set_group(1)
serial.write_line("Acceleration")

def on_received_number(receivedNumber):
    led.toggle(4, 4)
    serial.write_value("z", receivedNumber)
radio.on_received_number(on_received_number)


