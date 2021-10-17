from command import ICommand, SwitchOnCommand, SwitchOffCommand, Light, Switch


light = Light()
switch = Switch()
on_command = SwitchOnCommand(light)
off_command = SwitchOffCommand(light)

switch.register('LIGHT ON', on_command)
switch.register('LIGHT OFF', off_command)
switch.execute('LIGHT ON')
switch.execute('LIGHT OFF')

switch.get_history()
