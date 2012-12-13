node "default" {
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
}
    
