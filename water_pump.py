from gpiozero import OutputDevice
class Water_pump(OutputDevice):
    def fload(self):
        self.on()
    def stop(self):
        self.off()




