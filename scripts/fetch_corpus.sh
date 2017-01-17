#! /bin/bash

DAT='./corpus/' ;
if [ ! -d "${DAT}" ] ; then
    mkdir "${DAT}" ;
fi

TARBALL="${DAT}digits.tar.gz" ;
URL='http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishFnt.tgz' ;
if [ ! -e "${TARBALL}" ] ; then
    wget "${URL}" --output-document "${TARBALL}" ;
fi

TAR_DIRECTORY_FORMAT='English/Fnt/Sample%03d/' ;
for INDEX in {1..10} ; do
    TAR_DIRECTORY=$(printf "${TAR_DIRECTORY_FORMAT}" "${INDEX}") ;
    if [ ! -d "${DAT}${TAR_DIRECTORY}" ] ; then
        tar -xzvf "${TARBALL}" -C "${DAT}" "${TAR_DIRECTORY}" ;
    fi
done
