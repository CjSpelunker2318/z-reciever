basic.show_string("RECEIVER")
radio.set_group(56)
serial.write_line("Acceleration")

def on_received_number(receivedNumber):
    led.toggle(4, 4)
    serial.write_value("x", receivedNumber)
radio.on_received_number(on_received_number)

def on_received_number2(receivedNumber):
    led.toggle(4, 4)
    serial.write_value("y", receivedNumber)
radio.on_received_number(on_received_number2)

def on_received_number3(receivedNumber):
    led.toggle(4, 4)
    serial.write_value("z", receivedNumber)
radio.on_received_number(on_received_number3)

