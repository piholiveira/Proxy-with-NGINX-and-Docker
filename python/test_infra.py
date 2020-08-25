def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed

def test_docker_running(host):
    docker_running = host.service("docker")
    assert docker_running.is_running

def test_nginx_running(host):
    nginx_running = host.service("nginx")
    assert nginx_running.is_running

def test_file_app1_exists(host):
    file_app1 = host.file("/etc/nginx/sites-enabled/app1.dexter.com.br.conf").exists

def test_file_app2_exists(host):
    file_app2 = host.file("/etc/nginx/sites-enabled/app2.dexter.com.br.conf").exists

def test_file_app3_exists(host):
    file_app3 = host.file("/etc/nginx/sites-enabled/app3.dexter.com.br.conf").exists

def test_http_server(host):
    http = host.socket("tcp://0.0.0.0:80")
    assert http.is_listening

def test_port_app1_server(host):
    port_app1 = host.socket("tcp://0.0.0.0:8080")
    assert port_app1.is_listening

def test_port_app2_server(host):
    port_app2 = host.socket("tcp://0.0.0.0:8081")
    assert port_app2.is_listening

def test_port_app3_server(host):
    port_app3 = host.socket("tcp://0.0.0.0:8082")
    assert port_app3.is_listening

def test_container_app1(host):
    app1 = host.docker("app1")
    assert app1.is_running

def test_container_app2(host):
    app2 = host.docker("app2")
    assert app2.is_running

def test_container_app3(host):
    app3 = host.docker("app3")
    assert app3.is_running

def hosts_file_content(host):
    hosts = host.file ("/etc/hosts").content_string