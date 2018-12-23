#!/bin/bash
#waits the connection to be ready, speeds up bluetoothd and sets the ps3 gamepad to the slave mode.
btState="$(echo -e "info 05:34:9E:68:63:25\nquit" | bluetoothctl | grep "Connected" | cut --only-delimited --delimiter=' ' --fields=2)"

while [ "$btState" = "no" ]; do
        echo -e "connect 05:34:9E:68:63:25\nquit" | bluetoothctl >/dev/null 2>&1
        btState="$(echo -e "info 05:34:9E:68:63:25\nquit" | bluetoothctl | grep "Connected" | cut --only-delimited --delimiter=' ' --fields=2)"
        sleep 1
done

PID=`pgrep bluetoothd`
renice 10 -p $PID

hcitool sr 05:34:9E:68:63:25 slave

exit


