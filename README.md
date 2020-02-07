# Mantle
A Aplicação permite realizar backups automáticos de quantos directórios (localizações) que o utilizador pretenda :

Podemos agendar para realizar backups automáticos e ao final de um determinado numero de dias é realizado um novo backup caso exista diferenças no(s) directório(s) do backup.

Através da verificação das funções de hash é verificado se existe diferença entre o ficheiro de backup actual e o anterior caso exista o ficheiro novo é mantido caso não exista é apagado. 

Podemos ainda realizar backup cada vez que a aplicação é  re-aberta  que é o que acontece caso não seja agendado a realização de backups. 

O projecto foi realizado  em linguagem Python com recurso para a GUI de  PyQt.
