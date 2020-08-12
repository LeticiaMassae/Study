// pega as portas em um formato melhor
netstat -tulpn | grep LISTEN

ls -> List files and directories
  -l -> long output
  -a -> all files and directories
pwd -> Print out the current working directory
cd -> change the current working directory
clear -> clear the screen

~ -> alias for "my home directory"
. -> alias for "the current directory"
.. -> alias for "the parent directory"
"" -> Treat the enclosed text as a single Name
/ -> scape the following character
\ -> the root directory of the file system
<TAB> -> complete the name of a file or directory

mkdir -> make directory
  -p -> make parent directories if need
touch-> update last modified time, creating empty file if needed
  example: touch "my file"
cp -> copy files and directories
  -R -> recursively copy directory contents

  cat /etc/*-release
  yum install netcat
  yum whatprovides nc
  netstat -aln | grep 8080
  nc -l 8080
  - no cmd da minha maquina rodar:

curl localhost:27017

Advanced
sudo netstat -tulpn | grep LISTEN
netstat -lt

- Chech Firewall
sudo service iptables status

-Docker
docker image ls
docker ps
  docker ps -a
docker stop

- ver porta rodando
netstat -aln | grep 80
netstat -aln | grep 8080


Montando um EBS
https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/ebs-using-volumes.html
  lsblk
    - /dev/sdb -> volume não montado
    - Vira /dev/xvdb
  sudo file -s /dev/xvdb
  sudo yum install xfsprogs
  sudo mkfs -t xfs /dev/xvdb
  sudo mount /dev/xvdb /data



Montar automaticamente um volume anexado após a reinicialização
https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/ebs-using-volumes.html#ebs-mount-after-reboot
  sudo cp /etc/fstab /etc/fstab.orig
  sudo blkid
    - Retorno:
    - /dev/xvda1: LABEL="/" UUID="be4f19b3-a8ae-4d74-a7a0-b12b49e21194" TYPE="xfs" PARTLABEL="Linux" PARTUUID="d72fbb6a-12ee-4c53-aae4-330c552616b9"
    - /dev/xvdb: UUID="d3c656b4-233a-4af7-b6ee-6ea7e4ebd2db" TYPE="xfs"
    sudo vim /etc/fstab
    UUID=d3c656b4-233a-4af7-b6ee-6ea7e4ebd2db  /data  xfs  defaults,nofail  0  2
