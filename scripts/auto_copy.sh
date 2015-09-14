#!/bin/bash

# Copia cambios a web2py/applications/
# para kate?

HOMEPATH=$(echo ~)
APPNAME="mosivo"
LOCALPATH=$HOMEPATH"/workspace/"$APPNAME
echo "LOCALPATH: ${LOCALPATH}"
REMOTEPATH=""
echo "REMOTEPATH: ${REMOTEPATH}"
RSYNCCOMMAND="$LOCALPATH/scripts/rsync_with_w2p.py"

# get the current path
CURPATH=$(pwd)
EVENTS="CREATE,CLOSE_WRITE,DELETE,MODIFY,MOVED_FROM,MOVED_TO"
# kate events
#EVENTS="CREATE,DELETE,MOVED_TO"
FILETYPES="py js html css load sql json"
EXCLUDEDIRS="(.git|.gitignore|backup|export|qdgrsnd|scripts|tests)"

# bash function definition
doRsync() {
    # here $1 is the first parameter, $2 the second etc.
    FILECHANGE=${4}${5}
    # convert absolute path to relative
    FILECHANGEREL=$(echo "$FILECHANGE" | sed 's_'$CURPATH'/__')
    /usr/bin/python2 $RSYNCCOMMAND
    # rsync --progress --relative -vrae 'ssh -p 22' $FILECHANGEREL usernam@example.com:/backup/root/dir &&
    echo "At ${3} on ${2}, file $FILECHANGE was $1 event"
}

inotifywait -mr --exclude $EXCLUDEDIRS --timefmt '%d/%m/%y %H:%M' --format '%e %T %w %f' -e $EVENTS $LOCALPATH | while read event date time dir file; do
    FILEEXT=${file##*.}
    if [[ ${FILETYPES} =~ ${FILEEXT} ]]
    then
        doRsync $event $date $time $dir $file
    fi
done

