from ftplib import FTP
import subprocess
import gzip
import shutil

#  reponse à la question 1 : connexion au serveur ftp (ftp.free.fr)

f = FTP('ftp.free.fr')
print("Bonjour : ", f.getwelcome())
f.login()

#  reponse à la question 2:  afficher le chemin du répertoire courant

print(f"Le chemin du répertoire actuel est : {f.pwd()}")

#  reponse à la question 3 : afficher le contenu du répertoire courant

print("Voici les dossiers et fichiers du répertoire courant : ")
f.dir()

# reponse à la question 4: se déplacer dans le dossier ...

f.cwd('/pub/linux/kernel/ports/ppc/2.4/')
print("voici le contenu du dossier /pub/linux/kernel/ports/ppc/2.4/ : ")
f.dir()

# reponse à la question 5: télécharger le fichier ppc-patch-2.4.10.gz

fd = open('ppc-patch-2.4.10.gz', 'wb')
f.retrbinary('RETR ppc-patch-2.4.10.gz', fd.write)
fd.close()

#  reponse à la question 6: dézipper le fichier ppc-patch-2.4.10.gz et lire son contenu

with gzip.open('ppc-patch-2.4.10.gz', 'rb') as f_in:
    with open('ppc-patch-2.4.10.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
subprocess.call("nano ppc-patch-2.4.10.txt", shell=True)

f.quit()

