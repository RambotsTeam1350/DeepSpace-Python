import wpilib.joystick
import wpilib.xboxcontroller
import wpilib.buttons.button
import RobotMap


class OI:

    @staticmethod
    def getInstance():
        """Returns the Scheduler, creating it if one does not exist.

        :returns: the Scheduler
        """
        if not hasattr(OI, "instance"):
            OI.instance = OI()
        return OI.instance

    def __init__(self):

        self.leftstick = wpilib.joystick.Joystick(0)
        self.rightStick = wpilib.joystick.Joystick(1)
        self.xbox = wpilib.xboxcontroller.XboxController(RobotMap.xboxController)
        self.xboxControllerLeft = wpilib.joystick.Joystick(RobotMap.xboxController)
