class SmartWatch:
    def __init__(self):
        self.status = "OFF"
        self.battery_level = 100
        self.steps = 0
        self.heart_rate = 0

    def start(self):
        self.status = "ON"
        print("Smartwatch turned ON.")

    def stop(self):
        self.status = "OFF"
        print("Smartwatch turned OFF.")

    def track_steps(self, amount):
        self.steps += amount
        print("Steps updated to:", self.steps)

    def measure_heart_rate(self, rate):
        self.heart_rate = rate
        print("Heart rate updated to:", self.heart_rate, "BPM")

    def use_battery(self, amount):
        self.battery_level -= amount
        if self.battery_level < 0:
            self.battery_level = 0
        print("Battery decreased to:", self.battery_level, "%")

    def display_status(self):
        print("\n--- Smartwatch Status ---")
        print("Power:", self.status)
        print("Battery:", self.battery_level, "%")
        print("Steps:", self.steps)
        print("Heart Rate:", self.heart_rate, "BPM")





my_watch = SmartWatch()

print("Starting smartwatch:")
my_watch.display_status()

my_watch.start()
my_watch.track_steps(1500)
my_watch.measure_heart_rate(85)
my_watch.use_battery(10)

print("\nAfter using the smartwatch:")
my_watch.display_status()


my_watch.stop()


print("\nFinal smartwatch status:")
my_watch.display_status()