# Teste Prático

Durante o desenvolvimento utilizei ferramentas como Vagrant, Ansible e Python. O Vagrant foi utilizado para realizar todos os testes necessários de instalação, configuração, antes de implementar na máquina principal (GCP). Já o Ansible e Python, foi utilizado para implementar toda a infraestrutura onde o Ansible faz todo o trabalho de provisionar, e o Python vem após o ambiente ser provisionado testando portas, arquivos, serviços e pacotes.

## Informações: ##

|Arquivos|Descrição|
|-|-|
|main.yml|Instala, configura, e testa o Nginx e o Docker.|
|vars.yml|Variaveis de pastas de origem (máquina local).|
|install_docker.sh|Instala o Docker baseado na documentação oficial.|
|install_docker_compose.sh|Instala o Docker Compose baseado na documentação oficial.|
|run_docker_compose.sh|Roda o docker compose.|

## Referências ##
https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/
https://www.keycdn.com/support/nginx-virtual-host
https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-debian-9
https://docs.docker.com/engine/install/debian/
https://hub.docker.com/_/httpd
https://diagrams.mingrammer.com/docs

Dificuldades:
Obtive minha primeira dificuldade com o nginx, onde o obtive o erro "curl: (7) Failed to connect to 192.168.33.101 port 80: Connection refused" ao tentar acessa-lo.
No entanto, o erro estava no arquivo de configuração do virtual host em /etc/nginx/sites-avaliable/ somente com o nome app1.dexter.com.br não estava funcionando a conexão através do comando curl, sendo assim necessário colocar a extensão .conf para funcionar.
mv app1.dexter.com.br app1.dexter.com.br.conf, como fiz um link simbólico para a pasta de sites enabled, não foi necessário alterar neste repositorio também.