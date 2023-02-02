class ProControl:
    """!@brief	This class performs proportional control
        @details	This class performs proportional control
                    specifically for the motor position on the
                    motors in the ME_405 kit
    """
    def __init__(self, gain, setpoint, position):
        """!@brief	The constructor for the motor driver class
        @details	The constructor takes in initial settings for
                    gain and setpoint. For a step response the setpoint
                    should start at 0 and will later be changed by the
                    set_setpoint method
        @param	gain The initial gain for the proportional control loop
        @param	setpoint The initial setpoint for the control loop
        @param	position The current position of the item being controlled
        """
        self.gain = gain
        self.setpoint = setpoint
        #self.position = position
        
    def run(self,position)
        """!@brief	Runs the control loop
        @details	Executes one step of the control loop and
                    returns the effort
        @param	position The current position of the system
        """
        effort = self.gain*(self.setpoint-position)
        return effort
    def set_setpoint(self, new_setpoint)
        """@brief	Changes the setpoint for the system
        @details	Adjusts the setpoint for the control loop
                    for a step response this should be changed once
        @param	new_setpoint The desired setpoint for the system
        """
        self.setpoint = new_setpoint
        
    