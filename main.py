basic.show_string("RECEIVER")
radio.set_group(56)
serial.write_line("Acceleration")

def on_received_value(name, value):
    led.toggle(4,4)
    serial.write_value(name, value)
radio.on_received_value(on_received_value)

# def on_received_number(receivedNumber):
#     led.toggle(4, 4)
#     serial.write_value("x", receivedNumber)
# radio.on_received_number(on_received_number)

# def on_received_number2(receivedNumber):
#     led.toggle(4, 4)
#     serial.write_value("y", receivedNumber)
# radio.on_received_number(on_received_number2)

# def on_received_number3(receivedNumber):
#     led.toggle(4, 4)
#     serial.write_value("z", receivedNumber)
# radio.on_received_number(on_received_number3)

# def on_received_number4(receivedNumber):
#     led.toggle(1,4)
#     serial.write_value("degree", receivedNumber)
# radio.on_received_number(on_received_number4)