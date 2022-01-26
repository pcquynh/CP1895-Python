class Lightbub:
    def __init__(self, wattage: int, is_led: bool, brand_name: str, is_on: bool, brightness: int):
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_string(self):
        print(self.wattage, self.brand_name)

    def set_brightness(self, level):
        self.brightness = level
        print(f"Brightness level is {self.brightness}")


l1 =Lightbub(100, False, "Phillip", False, 2)
l1.to_string()
l1.set_brightness(6)