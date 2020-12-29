import click # click creates a good-looking cli!
from auth1 import app_cli
import time
from sys import exit

from auth1 import db

@app_cli.command("test", help="testing application backing connections. ")#command name is test and its function is giving help
#when we use "flask app --help" the above message is shown
def app_cli_test():
    status = True
    if test_database() is False:
        status = False
    #print ("###########-3")
    #print (status)
    if status:
        exit (0)
    else:
        exit (1)

def test_database():

    click.echo("Testing database connection ...........", nl=False)
    try:
        result = db.engine.execute("SELECT 1;").first()# check db connection
        # if command is executed, connected to the db, then bringing back the result ---> connection is ok
        #This can be any command other than select 1;
        if result[0] == 1:
            click.secho("SUCCESS", bold=True, fg="green")
            return True
            #return result #test
        else:
            click.secho("WARNING", bold=True, fg="yellow")# if command is executed,
            #but doesn't return 1 
            return True
            #return result#test

    except:
        click.secho("FAILED", bold=True, fg="red")
        return False
        #return result#test

 