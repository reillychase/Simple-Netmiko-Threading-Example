from multiprocessing import Pool

from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

# Define username and password to login to all routers with
USER = 'user'
PASSWORD = 'password'

# Define NetMiko device object for each router
ROUTERS = ['192.0.2.1', '192.0.2.2', '192.0.2.3', '192.0.2.4', '192.0.2.5',  '192.0.2.6', '192.0.2.7', '192.0.2.8', '192.0.2.9', '192.0.2.10',  '192.0.2.11', '192.0.2.12', '192.0.2.13', '192.0.2.14', '192.0.2.15']

#Command to run
COMMAND = 'show version'

#run a command and return tuple of router object, command run, result pass/fail, and command output or error message
def _runCommand(router, command):
    print('Running "{a}" on device {b}...'.format(a=command, b=router['ip']))
    output = (router, command, False, "Unknown Error Occurred")
    try:
        #Open SSH Session
        ssh_session = ConnectHandler(**router)
        #run command and set output
        output = (router, command, True, ssh_session.send_command(command))
        #Close SSH connection
        ssh_session.disconnect()
    except (NetMikoTimeoutException) as e:
        #NetMiko SSH Timeout
        output = (router, command, False, str(e))
    except (NetMikoAuthenticationException) as e:
        #NetMiko Authentication Failure
        output = (router, command, False, str(e))
    finally:
        return output
    #try_except
#def

#Pool.map helper to expand our Argument tuple and send to the real function
def runCommand(args):
    return _runCommand(*args)
#def

#main
if __name__ == '__main__':
    #Thread pool - connect to up to 5 devices simultaneously
    threadPool = Pool(5)

    #List of arguments to pass to threads
    threadArgs = []

    #loop through each router in our list
    for ROUTER in ROUTERS:
        DEVICE =  {'device_type': 'cisco_ios', 'ip': ROUTER, 'username': USER, 'password': PASSWORD, 'verbose': False, }
        #append a tuple of the netmike Device and the command to run for our ssh_session arguments
        threadArgs.append((DEVICE, COMMAND))
    #for

    #run our threads, gathering results into a list
    results = threadPool.map(runCommand, threadArgs)

    #print the pass/fail value of each result and the result output
    for result in results:
        print("{a}:\t{b}".format(a=result[2], b=result[3]))
#main
