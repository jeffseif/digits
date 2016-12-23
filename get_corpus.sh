#! /bin/bash

DAT='./corpus/' ;
cd "${DAT}" ;

TARBALL='digits.tar.gz' ;
URL='http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishFnt.tgz' ;
if [ ! -e "${TARBALL}" ] ; then
    curl "${URL}" --output "${TARBALL}" ;
fi

TAR_DIRECTORY_FORMAT='English/Fnt/Sample%03d/' ;
for INDEX in {1..10} ; do
    TAR_DIRECTORY=$(printf "${TAR_DIRECTORY_FORMAT}" "${INDEX}") ;
    if [ ! -d "${TAR_DIRECTORY}" ] ; then
        tar -xzvf "${TARBALL}" "${TAR_DIRECTORY}" ;
    fi
done
