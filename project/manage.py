from app import app
from flask.ext.script import Manager

##
#import models
##

from app.models.user import User


##
#create the manager
##
manager = Manager(app)


##
#add commands
##
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

##
#run the app
##

print app.config
print app.url_map

if __name__ == '__main__':
    manager.run()

