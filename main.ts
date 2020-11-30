basic.showString("RECEIVER")
radio.setGroup(1)
serial.writeLine("Acceleration")
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    led.toggle(4, 4)
    serial.writeValue("z", receivedNumber)
})
