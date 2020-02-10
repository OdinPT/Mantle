# Mantle
__PT_
A Aplicação permite realizar backups automáticos de quantos directórios (localizações) que o utilizador pretenda :

Podemos agendar para realizar backups automáticos e ao final de um determinado numero de dias é realizado um novo backup caso exista diferenças no(s) directório(s) do backup.

Através da verificação das funções de hash é verificado se existe diferença entre o ficheiro de backup actual e o anterior caso exista o ficheiro novo é mantido caso não exista é apagado. 

Podemos ainda realizar backup cada vez que a aplicação é  re-aberta  que é o que acontece caso não seja agendado a realização de backups. 

O projecto foi realizado  em linguagem Python com recurso para a GUI de  PyQt.

__EN__

The Application allows automatic backups of as many directories (locations) as the user wants:

We can schedule to perform automatic backups and at the end of a certain number of days a new backup is performed if there are differences in the backup directory (s).

By checking the hash functions, it is checked whether there is a difference between the current backup file and the previous one, if the new one exists, it is kept if none exists and is deleted.

We can also perform backup every time the application is re-opened, which is what happens if backups are not scheduled.

The project was carried out in Python using the PyQt GUI.
__
