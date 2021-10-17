from command import ICommand, SwitchOnCommand, SwitchOffCommand, Light, Switch


LIGHT = Light()
SWITCH = Switch()
on_command = SwitchOnCommand(LIGHT)
off_command = SwitchOffCommand(LIGHT)

SWITCH.register('LIGHT ON', on_command)
SWITCH.register('LIGHT OFF', off_command)

SWITCH.execute('LIGHT ON')
SWITCH.execute('LIGHT OFF')

SWITCH.get_history()
