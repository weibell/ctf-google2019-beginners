## day2-easy

**Work Computer** `[sandbox]`


```
> ls -lah /bin
total 808
drwxr-xr-x    2 65534    65534       4.0K Jun 13 14:28 .
drwxr-xr-x   20 0        0           4.0K Jun 13 14:28 ..
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 arch -> /bin/busybox
-rwxr-xr-x    1 65534    65534     777.6K Jan 24 07:45 busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 chgrp -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 chown -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 conspy -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 date -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 df -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 dmesg -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 dnsdomainname -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 dumpkmap -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 echo -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 false -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 fdflush -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 fsync -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 getopt -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 hostname -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ionice -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 iostat -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ipcalc -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 kill -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 login -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ls -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 lzop -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 makemime -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mkdir -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mknod -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mktemp -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mount -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mountpoint -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mpstat -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 netstat -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 nice -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pidof -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ping -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ping6 -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pipe_progress -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 printenv -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ps -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pwd -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 reformime -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 rm -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 rmdir -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 run-parts -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 setpriv -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 setserial -> /bin/busybox
-r-sr-xr-x    1 1338     1338       19.5K Jun 13 12:48 shell
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 sleep -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 stat -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 stty -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 sync -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 tar -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 true -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 umount -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 uname -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 usleep -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 watch -> /bin/busybox

> ls -lah /usr/bin
total 1992
drwxr-xr-x    2 65534    65534       4.0K Jun 13 14:28 .
drwxr-xr-x    8 65534    65534       4.0K Jun 13 14:28 ..
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 [ -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 [[ -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 basename -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 beep -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 blkdiscard -> /bin/busybox
-rwxr-xr-x    1 65534    65534      13.9K Jan 29 16:27 c_rehash
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 cal -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 chvt -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 cksum -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 clear -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 cpio -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 crontab -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 cryptpw -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 dc -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 deallocvt -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 dirname -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 dos2unix -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 du -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 eject -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 env -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 expr -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 factor -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 fallocate -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 flock -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 fold -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 free -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 fuser -> /bin/busybox
-rwxr-xr-x    1 65534    65534      35.9K Mar 19 09:56 getconf
-rwxr-xr-x    1 65534    65534      50.7K Mar 19 09:56 getent
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 groups -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 hostid -> /bin/busybox
-rwxr-xr-x    1 65534    65534      24.6K Mar 19 09:56 iconv
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 id -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 install -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ipcrm -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ipcs -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 killall -> /bin/busybox
lrwxrwxrwx    1 65534    65534         29 May  9 20:49 ldd -> ../../lib/ld-musl-x86_64.so.1
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 logger -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 lsof -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 lsusb -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 lzcat -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 lzma -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 lzopcat -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 md5sum -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mesg -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 microcom -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mkfifo -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 mkpasswd -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 nmeter -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 nohup -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 nproc -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 nsenter -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 nslookup -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 openvt -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 passwd -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 patch -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pgrep -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pkill -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pmap -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 printf -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pstree -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 pwdx -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 readlink -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 realpath -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 renice -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 reset -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 resize -> /bin/busybox
-rwxr-xr-x    1 65534    65534      81.8K Nov 15  2018 scanelf
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 seq -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 setkeycodes -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 setsid -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 sha1sum -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 sha256sum -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 sha3sum -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 sha512sum -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 showkey -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 shred -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 shuf -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 smemcap -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 split -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 sum -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 test -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 time -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 timeout -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 top -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 truncate -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 tty -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 ttysize -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 udhcpc6 -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 unix2dos -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 unlink -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 unlzma -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 unlzop -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 unshare -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 unxz -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 uptime -> /bin/busybox
-rwxr-xr-x    1 65534    65534       1.7M Dec 28 07:46 upx
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 vlock -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 volname -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 wc -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 which -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 whoami -> /bin/busybox
lrwxrwxrwx    1 65534    65534         12 May  9 20:49 yes -> /bin/busybox
```

