import datetime
import hashlib
import os.path
import pathlib
import shutil
import sys
import zipfile as zipf
from PyQt5.QtWidgets import *
from Qt import QtGui
from future.backports.datetime import timedelta
from datetime import date, timedelta
from formWin import *
from sys import platform as _platform

logfile = 'logBackup.conf'

def gennamefile():
 today = str(date.today())
 filex = ('backup_' + today +'.zip')
 return filex

def ReturnNameBackup(name):
 file = ('backup_' + name.rstrip() +'.zip')
 return file

def FileLogBackups(nomefile):    # vou buscar ultimo registo e verifico se o ultimo registo é o dia atual se for salta fora.
  datex = str(datetime.date.today())

  lf = pathlib.Path("logBackup.conf")
  if lf.exists():
     print("existe lg")

     with open(nomefile, "r+") as f:
         a = f.read()
         #print(a)
         with open(nomefile, "w+") as f:
             f.write(datex + "\n" + a)

  else:     #cria novo ficheiro e insere a data do dia atual
     print("lg not exist")
     with open(nomefile, 'w') as myFile:
         myFile.write(datex)

def ReadFirstLine(nomefile):
  with open(nomefile) as f:
    first_line = f.readline()
    return first_line

class Main(Dialog):

 def zipar(arqs):

   today = str(datetime.date.today())
   filex = gennamefile()

   ReadLastRegtLog = (ReadFirstLine('logBackup.conf'))
   Teste = ReadLastRegtLog.rstrip('\n')
   ReadLastString = str(Teste)

   ReadToday = str(today)
   print(ReadLastString+ "\n"+ today)

   if ReadLastString == ReadToday :
    print(" ")
   else :
       print("Making Backup ")
       FileLogBackups(logfile)
       with zipf.ZipFile(filex, 'w', zipf.ZIP_DEFLATED) as z:
           for arq in arqs:
               if (os.path.isfile(arq)):  # se for ficheiro
                   z.write(arq)
               else:  # se for diretorio
                   for root, dirs, files in os.walk(arq):
                       for f in files:
                          z.write(os.path.join(root, f))


 def ReadSecundLine(nomefile):
  line = open(nomefile, "r").readlines()[1]
  return line

 def ReturnDateNextBackup(DataAnt, timebackup):
        # recebe temp e timeBackup e retorna
     date_time_obj = datetime.datetime.strptime(str(DataAnt), '%Y-%m-%d ')
     temp = date_time_obj.date()
     d = temp + timedelta(days=(int(timebackup)))
     return d

 def Sha1Hasher(file_path):

     buf_size = 65536
     sha1 = hashlib.sha1()

     with open(file_path, 'rb') as f:
         while True:
             data = f.read(buf_size)
             if not data:
                 break
             sha1.update(data)

     return format(sha1.hexdigest())

 if __name__ == '__main__':

  file = pathlib.Path("definitions.conf")
  file2 = pathlib.Path("logBackup.conf")

  if file.exists()  == 1:
       print("File exist \n")             # le o ficheiro e procura pelo diretório  a fazer backup #

       with open('definitions.conf') as myfile:
        data = "|".join(line.rstrip() for line in myfile)

        #separa as localizações do ficheiro | e coloca cada uma numa row do array
        x = data.split("|")
        for b in range(len(x)):
            q = x[b].split("/")
            BName = (q[-2])

            #se não existir ficheiro de Time faz backup a mesma  e depois de gerar ficheiro componho o ficheiro e verifico
            # as funções de hash

            file3 = pathlib.Path("Time_Backup.conf")

            if file3.exists() == 1:
                print ("if 1")

                timebackup = ReadFirstLine('Time_Backup.conf')
                DataAnt = ReadFirstLine(logfile)

                print("Days to Backup : ")
                print(timebackup)
                print("Next Backup is :")

                NextBackup = ReturnDateNextBackup(DataAnt,timebackup)
                nextbackupstr = str(NextBackup)
                print(nextbackupstr)
                print("\n   ")

                today = str(date.today())


                if today == nextbackupstr:

                    print("if 2")
                    # gera nome dos ficheiros de backup a partir do log
                    print("\nreadfirst line ")
                    OldFile = ReturnNameBackup(DataAnt)
                    print("secund file is" + OldFile)

                    print("\nread Secund  line ")
                    ReadSecundReg = ReadSecundLine(logfile)
                    NewFile = ReturnNameBackup(ReadSecundReg)

                    # retorna sha1 do ficheiro backup
                    SHA1FFile = Sha1Hasher(OldFile)

                    SHA2File = Sha1Hasher(NewFile)
                    print(SHA2File)

                    if SHA1FFile == SHA2File:
                      print("\n \n if 3 ==>")
                      os.remove(OldFile)
                      #zipar([x[b]])
                    else:
                     zipar([x[b]])
            else:

             zipar([x[b]])

             print ("penultimo else 1")

             Datatual = ReadFirstLine(logfile)
             print ("176 Today "+ Datatual)

             ReadSecundReg = ReadSecundLine(logfile)
             print("181 line  Last day " + ReadSecundReg)

             NFile = ReturnNameBackup(Datatual)
             print(" new file name ==-_" + NFile)
             OldFile = ReturnNameBackup(ReadSecundReg)
             print (" name old file : => " + OldFile)
             # retorna sha1 do ficheiro backup

            #verifica se existe ficheiro anterior
            file4 = pathlib.Path(OldFile)
            if file4.exists():

                SHA11File = str(Sha1Hasher(OldFile))
                print(SHA11File)

                SHA2File = str(Sha1Hasher(NFile))
                print(SHA2File)

                if SHA11File == SHA2File :
                    print(" \n \n if 4")
                    print("equals")
                    os.remove(OldFile)
                else:
                    #data in files is diferent
                    print("Diferent files")
                    filebackup = pathlib.Path('Backups')

                    if filebackup.exists():
                        print("existe dir backup")
                    else:
                        dir = os.mkdir('Backups/')

                    temp = 'Old_File.' + OldFile
                    #Change name file

                    #os.rename(OldFile, temp)

                    #move file
                    shutil.copy2(temp, 'Backups/');
                    #os.remove(temp)
                    _platform ="win64"

                    if _platform == "linux" or _platform == "linux2":
                        print(" linux")
                    elif _platform == "darwin":
                        print(" Mac os ")
                    elif _platform == "win64":
                        print(" Windows X ")

            else:
                print("Não existe ficheiro anterior")

  else:
        print("File not exist")
        app = QApplication([])
        w = Dialog()
        w.show()

        sys.exit(app.exec_())

    # antes der ver de copiar para desktop ver como ver por ifs se é windows ou linux
