# ps3controller
Battery monitor UI for the ps3 controller and bluetooth slave scripts

To pair the ps3 gamepad, download and compile the sixpair.c file:
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb 

Connect the gamepad via usb and run the command: sudo ./sixpair.
Accept bluetooth pairing with a bluetooth client software.

To speed up Bluetooth connection, set the ps3 controller from master to slave, boost the bluetoothd process and buy a faster adapter.

Here are the udev rule for the /lib/udev/rules.d/60-joystick.rules file , the /etc/systemd/system/ps3gamepad.service file and slaveit.sh file that you must make executable with chmod a+x. Run sudo 
systemctl daemon-reload to enable the new service. Run sudo udevadm control --reload to reload rules without rebooting. Restart the systemd bluetooth service to shut down the ps3 gamepad.

ACTION=="add", KERNEL=="js*", IMPORT{parent}="DEVPATH", ATTRS{name}=="PLAYSTATION(R)3Controller",TAG+="systemd", ENV{SYSTEMD_WANTS}="ps3gamepad.service"

For Shanwan/Panhai PS3 gamepad, have in: /var/lib/bluetooth/00:1A:7D:DA:71:11/cache# cat 05\:34\:9E\:68\:63\:25 
[ServiceRecords]
0x00010000=3601920900000A000100000900013503191124090004350D35061901000900113503190011090006350909656E09006A0901000900093508350619112409010009000D350F350D350619010009001335031900110901002513576972656C65737320436F6E74726F6C6C65720901012513576972656C65737320436F6E74726F6C6C6572090102251B536F6E7920436F6D707574657220456E7465727461696E6D656E740902000901000902010901000902020800090203082109020428010902052801090206359A35980822259405010904A101A102850175089501150026FF00810375019513150025013500450105091901291381027501950D0600FF8103150026FF0005010901A10075089504350046FF0009300931093209358102C0050175089527090181027508953009019102750895300901B102C0A1028502750895300901B102C0A10285EE750895300901B102C0A10285EF750895300901B102C0C0090207350835060904090901000902082800090209280109020A280109020B09010009020C093E8009020D280009020E2800
