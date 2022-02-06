import turtle
from datetime import *

# Clock Using Turtle
def turtle_clock():
    # Lift the paintbrush and move it forward for a distance
    def Skip(step):
        turtle.penup()
        turtle.forward(step)
        turtle.pendown()

    def mkHand(name, length):
        # Register the Turtle shape and create the hand Turtle
        turtle.reset()
        Skip(-length * 0.1)
        # Start recording the vertices of the polygon. The current turtle position is the first vertex of the polygon.
        turtle.begin_poly()
        turtle.forward(length * 1.1)
        # Stop recording the vertices of the polygon. The current turtle position is the last vertex of the polygon. Will be connected to the first vertex.
        turtle.end_poly()
        # Return the last recorded polygon.
        handForm = turtle.get_poly()
        turtle.register_shape(name, handForm)

    def Init():
        global secHand, minHand, hurHand, printer
        # Reset Turtle to point north
        turtle.mode("logo")
        # Create three hands Turtle and initialize
        mkHand("secHand", 135)
        mkHand("minHand", 125)
        mkHand("hurHand", 90)
        secHand = turtle.Turtle()
        secHand.shape("secHand")
        minHand = turtle.Turtle()
        minHand.shape("minHand")
        hurHand = turtle.Turtle()
        hurHand.shape("hurHand")

        for hand in secHand, minHand, hurHand:
            hand.shapesize(1, 1, 3)
            hand.speed(0)

        # Create output text Turtle
        printer = turtle.Turtle()
        # Hide the turtle shape of the brush
        printer.hideturtle()
        printer.penup()

    def SetupClock(radius):
        # Create a table frame
        turtle.reset()
        turtle.pensize(7)
        for i in range(60):
            Skip(radius)
            if i % 5 == 0:
                turtle.forward(20)
                Skip(-radius - 20)

                Skip(radius + 20)
                if i == 0:
                    turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
                elif i == 30:
                    Skip(25)
                    turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                    Skip(-25)
                elif (i == 25 or i == 35):
                    Skip(20)
                    turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                    Skip(-20)
                else:
                    turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-radius - 20)
            else:
                turtle.dot(5)
                Skip(-radius)
            turtle.right(6)

    def Week(t):
        week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        return week[t.weekday()]

    def Date(t):
        y = t.year
        m = t.month
        d = t.day
        return "%s %d% d" % (y, m, d)

    def Tick():
        # Draw the dynamic display of hands
        t = datetime.today()
        second = t.second + t.microsecond * 0.000001
        minute = t.minute + second / 60.0
        hour = t.hour + minute / 60.0
        secHand.setheading(6 * second)
        minHand.setheading(6 * minute)
        hurHand.setheading(30 * hour)

        turtle.tracer(False)
        printer.forward(65)
        printer.write(Week(t), align="center",
                      font=("Courier", 14, "bold"))
        printer.back(130)
        printer.write(Date(t), align="center",
                      font=("Courier", 14, "bold"))
        printer.home()
        turtle.tracer(True)

        # Continue to call tick after 100ms
        turtle.ontimer(Tick, 100)

    def main():
        # Turn on / off turtle animation and set a delay for updating drawings.
        turtle.tracer(False)
        Init()
        SetupClock(160)
        turtle.tracer(True)
        Tick()
        turtle.title("Turtle Graphic Clock")
        turtle.mainloop()

    if __name__ == "__main__":
        main()
