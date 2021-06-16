import shoot as shoot
from evennia import command

class cmdshoot(shoot):
    key = "shoot"
    aliases = ["fire", "fire!"]

    def func(self):
        caller = self.caller
        location = caller.location

        if not self.args:
            message = "Boom! The mech fires its gun into the air!"
            location.msg_contents(message)
            return

        target = caller.search(self.args.strip())
        if target:
            message = "Boom! The mech fires it's gun at %s" % target.key
            location.msg_contents(message)

class cmdlaunch(command):
    key = "launch"
    aliases = ["launch!"]

    def func(self):
        caller = self.caller
        location = caller.location

        if not self.args:
            message = "Whoosh! The mech launches a missile wildly into the sky!"
            location.msg_contents(message)
            return

        target = caller.search(self.args.strip())
        if target:
            message = "Whoosh! The mech launches a missile into %s" % target.key
            location.msg_contents(message)

