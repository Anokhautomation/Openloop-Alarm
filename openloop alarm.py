from machine import Pin,PWM
from utime import sleep
loop_sensor = Pin(16,Pin.IN,Pin.PULL_UP)#connect a wire Gp16 and GND via 10K resistance
led = Pin(15,Pin.OUT)
buzzer = PWM(Pin(13))
while True:
    if loop_sensor.value()==1:
        led.toggle()
        buzzer.freq(500)#Buzzer will start to beep according to the frequency and duty.
        buzzer.duty_u16(90000)
        sleep(0.5)
        buzzer.duty_u16(0)
        sleep(0.05)
        buzzer.duty_u16(1)
    else:
        led.off()
        buzzer.deinit()