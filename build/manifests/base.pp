node "default" {
  user { "vagrant":
     ensure => present,
     groups => [mock],
     require => Package['mock']
  }
  package { "mock": ensure => latest }
  package { "rpm-build": ensure => latest }
  package { "fedora-packager": ensure => latest }

  file { "/home/vagrant/rpmbuild":
    ensure => directory;
  }
  file { "/home/vagrant/rpmbuild/RPMS":
    ensure => directory;
  }
  file { "/home/vagrant/rpmbuild/RPMS/x86_64":
    ensure => directory;
  }
  file { "/home/vagrant/rpmbuild/RPMS/x386":
    ensure => directory;
  }
  file { "/home/vagrant/rpmbuild/SRPMS":
    ensure => link,
    target => "/home/vagrant/build/SRPMS",
    force => true
  }
  file { "/home/vagrant/rpmbuild/BUILD":
    ensure => directory;
  }
  file { "/home/vagrant/rpmbuild/SPECS":
    ensure => link,
    target => "/home/vagrant/build/SPECS",
    force => true
  }
  file { "/home/vagrant/rpmbuild/SOURCES":
    ensure => link,
    target => "/home/vagrant/build/SOURCES",
    force => true
  }
  file { "/home/vagrant/.rpmmacros":
    ensure => present,
    content => '
%_topdir %(echo $HOME)/rpmbuild

%_smp_mflags %( \
    [ -z "$RPM_BUILD_NCPUS" ] \\\
        && RPM_BUILD_NCPUS="`/usr/bin/nproc 2>/dev/null || \\\
                             /usr/bin/getconf _NPROCESSORS_ONLN`"; \\\
    if [ "$RPM_BUILD_NCPUS" -gt 16 ]; then \\\
        echo "-j16"; \\\
    elif [ "$RPM_BUILD_NCPUS" -gt 3 ]; then \\\
        echo "-j$RPM_BUILD_NCPUS"; \\\
    else \\\
        echo "-j3"; \\\
    fi )

%__arch_install_post \
    [ "%{buildarch}" = "noarch" ] || QA_CHECK_RPATHS=1 ; \
    case "${QA_CHECK_RPATHS:-}" in [1yY]*) /usr/lib/rpm/check-rpaths ;; esac \
    /usr/lib/rpm/check-buildroot
'
  }

  # Add mock definitions for python, ruby, and scl (the latter is to build the python27-build and ruby193-build packages)

  file { "/etc/mock/python27-x86_64.cfg":
    path => "/etc/mock/python27-x86_64.cfg",
    content => template("python27-x86_64.cfg.erb"),
  }

  file { "/etc/mock/ruby193-x86_64.cfg":
    path => "/etc/mock/ruby193-x86_64.cfg",
    content => template("ruby193-x86_64.cfg.erb"),
  }

  file { "/etc/mock/scl-x86_64.cfg":
    path => "/etc/mock/scl-x86_64.cfg",
    content => template("scl-x86_64.cfg.erb"),
  }

  file { "/etc/mock/python33-x86_64.cfg":
    path => "/etc/mock/python33-x86_64.cfg",
    content => template("python33-x86_64.cfg.erb"),
  }

  file { "/etc/mock/php54-x86_64.cfg":
    path => "/etc/mock/php54-x86_64.cfg",
    content => template("php54-x86_64.cfg.erb"),
  }

  file { "/etc/mock/perl516-x86_64.cfg":
    path => "/etc/mock/perl516-x86_64.cfg",
    content => template("perl516-x86_64.cfg.erb"),
  }

  file { "/etc/mock/postgres92-x86_64.cfg":
    path => "/etc/mock/postgres92-x86_64.cfg",
    content => template("postgres92-x86_64.cfg.erb"),
  }

  file { "/etc/mock/mysql55-x86_64.cfg":
    path => "/etc/mock/mysql55-x86_64.cfg",
    content => template("mysql55-x86_64.cfg.erb"),
  }

  file { "/etc/mock/node010-x86_64.cfg":
    path => "/etc/mock/node010-x86_64.cfg",
    content => template("node010-x86_64.cfg.erb"),
  }


}


