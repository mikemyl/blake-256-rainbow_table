"""Receiver DBus python script."""
import gobject
import dbus
import dbus.service
import dbus.glib
import time
import os


def catchall_handler(*args, **kwargs):
    """Catch the dbus - message."""
    print ("Caught signal: " + kwargs['dbus_interface'] + "." + kwargs[
        'member'])
    myfile = open('receivernetstat.dat', 'a+')
    myfile.write("\n" + time.strftime("%b %d %Y %H:%M:%S") + (
        " Caught signal: " + (
            kwargs['dbus_interface'] + "." + kwargs['member'])))
    for arg in args:
        print (arg)
        myfile.write("\n" + time.strftime("%b %d %Y %H:%M:%S") + ' ' + arg)
    p_netstat = os.popen('netstat -an').read()
    myfile.write("\n NETSTAT output \n" + time.strftime(
        "%b %d %Y %H:%M:%S") + '\n' + p_netstat)
    myfile.close()


def main():
    """Register to dbus and run the main loop."""
    print "Starting script"
    loop = gobject.MainLoop()
    session_bus = dbus.SessionBus()

    session_bus.add_signal_receiver(catchall_handler, interface_keyword=(
        'dbus_interface'), member_keyword='member')
    loop.run()

if __name__ == "__main__":
    main()
