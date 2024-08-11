class MockGPIO:
    BCM = "BCM"
    OUT = "OUT"
    HIGH = True
    LOW = False

    def __init__(self):
        self.pins = {}

    def setmode(self, mode):
        print(f"Set mode: {mode}")

    def setup(self, pin, state):
        print(f"Setup pin {pin} as {state}")
        self.pins[pin] = self.LOW

    def output(self, pin, state):
        print(f"Set pin {pin} to {'HIGH' if state else 'LOW'}")
        self.pins[pin] = state

    def cleanup(self):
        print("Cleanup GPIO")
        self.pins = {}

# Replace RPi.GPIO with MockGPIO in your code
GPIO = MockGPIO()
