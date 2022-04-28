FROM scratch
ADD files/alpine-minirootfs-3.15.4-x86_64.tar.gz
CMD [ "/bin/sh" ]