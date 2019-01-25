import wpilib
from wpilib.drive import DifferentialDrive
import wpilib.command.subsystem
import OI
import RobotMap


class DriveTrain(wpilib.command.subsystem):

    xPressed = False

    def robotInit(self):
        """Robot initialization function"""

        # object that handles basic drive operations
        self.leftMotorController = wpilib.VictorSP
        self.rightMotorController = wpilib.VictorSP
        #self.tankDrive = TELEOP
        self.robotDrive = wpilib.drive

        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

        self.timer = wpilib.Timer()

    def initialize(self):
        leftMotorController = wpilib.VictorSP(RobotMap.leftMotor)
        rightMotorController = wpilib.VictorSP(RobotMap.rightMotor)

        self.robotDrive = wpilib.drive.DifferentialDrive(leftMotorController, rightMotorController)

    def initDefaultCommand(self):
        wpilib.command.subsystem.Subsystem.setDefaultCommand(self, tankDrive)

    @staticmethod
    def getInstance():
        """Returns the Scheduler, creating it if one does not exist.

        :returns: the Scheduler
        """
        if not hasattr(DriveTrain, "instance"):
            DriveTrain.instance = DriveTrain()
        return DriveTrain.instance

    def tankDrive(self, left, right, squaredInputs):
        DriveTrain.robotDrive.tankDrive(left, right, squaredInputs)

    def getXPressed(self):
        if OI.OI.getInstance().xbox.getXButtonPressed() and DriveTrain.xPressed == False:
            xPressed = True
        if OI.OI.getInstance().xbox.getXButtonPressed() and DriveTrain.xPressed == True:
            xPressed = False

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        self.myRobot.tankDrive(self.leftStick.getY() * -1, self.rightStick.getY() * -1)


if __name__ == "__main__":
    wpilib.run(MyRobot)