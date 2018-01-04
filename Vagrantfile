# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos6.5"
  config.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_centos-6.5_chef-provisionerless.box"
  config.vm.network :private_network, ip: "192.168.33.10"
  config.vm.provision :shell, privileged: false, inline: <<-EOT
sudo yum groupinstall -y "Development tools"
sudo yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel

PYTHON_VERSION=2.7.14
git clone https://github.com/tagomoris/xbuild.git
xbuild/python-install ${PYTHON_VERSION} ~/local/python
echo 'export PATH=~/local/python/bin:$PATH' >> ~/.bashrc

APPENGINE_ZIP=google_appengine_1.9.65.zip
wget -q --no-check-certificate https://storage.googleapis.com/appengine-sdks/featured/${APPENGINE_ZIP}
unzip ${APPENGINE_ZIP}
echo 'export PATH=~/google_appengine:$PATH' >> ~/.bashrc
echo 'alias dev_appserver.py="dev_appserver.py --host 192.168.33.10 --admin_host 192.168.33.10"' >> ~/.bashrc
echo 'alias appcfg.py="appcfg.py --noauth_local_webserver"' >> ~/.bashrc
  EOT

end
