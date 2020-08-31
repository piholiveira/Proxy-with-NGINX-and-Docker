# VirtualHosts e Proxy_Pass com NGINX e Docker. #
<p align="center"> <img src="https://img.shields.io/badge/Supported OS-Linux-Orange" alt=""> <img src="https://img.shields.io/badge/Using-Docker-Orange" alt=""> <img alt="Docker Image Size (tag)" src="https://img.shields.io/docker/image-size/pirodriguees/app2/1.0"> <img src="https://img.shields.io/badge/nginx-v1.10.3-blue" alt=""> <img src="https://img.shields.io/badge/httpd-v2.4-blue" alt=""></p>


## Objetivo: ##
Instalar NGINX e Docker em uma máquina virtual na GCP, criar três Virtualhosts no NGINX para app1.dexter.com.br, app2.dexter.com.br, app3.dexter.com.br, e implementar proxy_pass para os containers Docker de nome app1, app2, e app3 com cada um deles rodando Apache.

Durante o desenvolvimento utilizei ferramentas como Vagrant, Ansible e Python. O Vagrant foi utilizado para realizar todos os testes necessários de instalação, configuração, antes de implementar na máquina principal (GCP). Já o Ansible e Python, foi utilizado para implementar toda a infraestrutura onde o Ansible faz todo o trabalho de provisionar, e o Python vem após o ambiente ser provisionado testando portas, arquivos, serviços e pacotes.

## Informações: ##

|Arquivos|Descrição|
|-|-|
|main.yml|Instala, configura, e testa o Nginx e o Docker.|
|vars.yml|Variaveis de pastas de origem (máquina local).|
|install_docker.sh|Instala o Docker baseado na documentação oficial.|
|install_docker_compose.sh|Instala o Docker Compose baseado na documentação oficial.|
|run_docker_compose.sh|Roda o docker compose.|
|app*.dexter.com.br.conf|Arquivo de configuração do NGINX|
|docker-compose.yml|Nomeia os containers, baixa e executa as imagens, e faz o bind das portas.|
|stack.png|Imagem da documentação gerada com Python Diagrams|

## Resultado: ##

![stack](https://user-images.githubusercontent.com/52767137/91721313-f1919000-eb6e-11ea-88df-7fdc124017df.png)

## Referências ##
- [Documentação NGINX](https://docs.nginx.com/)
- [Documentação Ansible](https://docs.ansible.com/ansible/latest/index.html)
- [Documentação Diagrams](https://diagrams.mingrammer.com/docs/getting-started/installation)
- [Documentação Testinfra](https://testinfra.readthedocs.io/en/latest/)
- [Docker Hub httpd.](https://hub.docker.com/_/httpd)
- [Keycdn - NGINX Virtualhosts.](https://www.keycdn.com/support/nginx-virtual-host)
- [Digitalocean proxy_pass.](https://www.digitalocean.com/community/tutorials/understanding-nginx-http-proxying-load-balancing-buffering-and-caching)
- [Rafael Gomex, teste de infraestrutura.](https://www.youtube.com/watch?v=ZVHlKWLEyhE&t=1558s)
- [Documentation as Code.](https://www.youtube.com/watch?v=eI7jbBtnFrg)
- [João Maia - Desenhando infra.](https://blog.joaovrmaia.com/post/desenhando-infraestrutura-com-codigo/)