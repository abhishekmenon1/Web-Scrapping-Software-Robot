from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def open_browser():
    robot.open_webpage("https://www.wikipedia.com")


def main():
    introduce_yourself()
    open_browser()

if __name__ == "__main__":
    main()

