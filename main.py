basic.show_string("RECEIVER")
radio.set_group(56)
serial.write_line("Acceleration")

def on_received_value(name, value):
    led.toggle(4,4)
    serial.write_value(name, value)
radio.on_received_value(on_received_value)
