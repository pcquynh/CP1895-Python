class Lightbub:
    def __init__(self, wattage: int, is_led: bool, brand_name: str, is_on: bool=False):
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_string(self):
        print(self.wattage, self.brand_name)


    def set_brightness(self, level):
        print(f"Brightness level is {level}")


l1 = Lightbub(100, False, "Phillip" )
l1.to_string()
l1.set_brightness(5)