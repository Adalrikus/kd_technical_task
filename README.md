# kd_technical_task
DevOps task: Create stack Hashicorp Nomad+Consul+Ansible+Flask+NGINX

## Prerequisites:
* Vagrant
* VirtualBox
* Ansible

## Deployment procedure:
Clone the repository

    git clone https://github.com/Adalrikus/kd_technical_task.git

Start VMs

    vagrant up

**NOTE: Install vagrant-vbguest beforehand:**

    vagrant plugin install vagrant-vbguest

**NOTE: edit ansible with your ips and ssh keys:**

    vim inventory

Change consul and nomad versions to latest

    vim ansible-role-consul/defaults/main.yml

    vim ansible-role-nomad/defaults/main.yml

Provision your software with Ansible

    ansible-playbook playbook.yml -i inventory

Run Nomad jobs

    vagrant ssh node2/3/4

    cd /vagrant/jobs

    nomad run flask.nomad

    nomad run nginx.nomad

Set up complete!
