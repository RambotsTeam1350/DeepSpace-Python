import wpilib
import wpilib.command
import OI


class Robot(wpilib.timedrobot):

    def __init__(self):
        limitswitch1 = wpilib.digitalinput

        m_autonomousCommand = wpilib.command.command
        # need to add SendableCoosers (for SmartDashboard)

    def robotInit(self):
        self.oi = OI.OI.getInstance()

        limitswitch1 = wpilib.digitalinput.DigitalInput(1)

    def autonomousInit(self, m_autonomousCommand):
        """Called only at the beginning of autonomous mode"""

        #Add Sendable Chooser here

        if m_autonomousCommand != None:
            m_autonomousCommand.start()

    def autonomousPeriodic(self):
        """Called every 20ms in autonomous mode"""
        wpilib.command.Scheduler.getInstance().run()

    def disabledInit(self):
        """Called only at the beginning of disabled mode"""
        pass

    def disabledPeriodic(self):
        """Called every 20ms in disabled mode"""
        wpilib.command.Scheduler.getInstance().run()

    def teleopInit(self, m_autonomousCommand):
        """Called only at the beginning of teleoperated mode"""

        if m_autonomousCommand != None:
            m_autonomousCommand.cancel()

    def teleopPeriodic(self):
        """Called every 20ms in teleoperated mode"""

        wpilib.command.Scheduler.getInstance().run(self)

        # Move a motor with a Joystick
        #self.motor.set(self.lstick.getY())

if __name__ == "__main__":
    wpilib.run(Robot)