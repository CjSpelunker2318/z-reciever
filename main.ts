basic.showString("RECEIVER")
radio.setGroup(56)
serial.writeLine("Acceleration")
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    led.toggle(4, 4)
    serial.writeValue("x", receivedNumber)
})
radio.onReceivedNumber(function on_received_number2(receivedNumber: number) {
    led.toggle(4, 4)
    serial.writeValue("y", receivedNumber)
})
radio.onReceivedNumber(function on_received_number3(receivedNumber: number) {
    led.toggle(4, 4)
    serial.writeValue("z", receivedNumber)
})
