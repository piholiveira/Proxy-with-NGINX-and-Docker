from diagrams import Cluster, Diagram
from diagrams.onprem.network import Apache
from diagrams.gcp.network import VPC
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Nginx
from diagrams.gcp.network import Routes


with Diagram("Stack", show=False):
    with Cluster("GCP"):
        dns1 = Routes("app1.com.br")
        dns2 = Routes("app2.com.br")
        dns3 = Routes("app3.com.br")

        with Cluster("VPC"):
            google_vpc = VPC("VPC Google Cloud")
            nginx = Nginx("Virtualhosts - Proxy_Pass")
            docker_app1 = Docker("app1")
            docker_app2 = Docker("app2")
            docker_app3 = Docker("app3")
            apache_app1 = Apache("index.html")
            apache_app2 = Apache("index.html")
            apache_app3 = Apache("index.html")

            dns3 >> google_vpc >> nginx >> docker_app1 >> apache_app3
            dns2 >> google_vpc  >> nginx >> docker_app2 >> apache_app2
            dns1 >> google_vpc >> nginx >> docker_app3 >> apache_app1