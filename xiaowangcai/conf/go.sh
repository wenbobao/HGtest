#!/bin/bash
if [ ! -n "$1" ]
then
    echo "Usages: sh go.sh [start|stop|restart]"
    exit 0
fi

if [ $1 = start ]
then
    psid=`ps aux | grep "uwsgi" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ]
    then
        echo "uwsgi is running!"
        exit 0
    else
        uwsgi --ini /service/shouzhuan/conf/uwsgi.ini
        echo "Start uwsgi service [OK]"
    fi
 

elif [ $1 = stop ];then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
    killall -9 uwsgi
    uwsgi --ini /service/shouzhuan/conf/uwsgi.ini
    echo "Restart uwsgi service [OK]"

else
    echo "Usages: sh go.sh [start|stop|restart]"
fi
