# Sensible Perl-specific RPM build macros.
#
# Note that these depend on the generic filtering system being in place in
# rpm core; but won't cause a build to fail if they're not present.
#
# Chris Weyl <cweyl@alumni.drew.edu> 2009

# keep track of what "revision" of the filtering we're at.  Each time we
# change the filter we should increment this.

%perl_default_filter_revision 2

# By default, for perl packages we want to filter all files in _docdir from 
# req/prov scanning, as well as filtering out any provides caused by private 
# libs in vendorarch/archlib (vendor/core).
#
# Note that this must be invoked in the spec file, preferably as 
# "%{?perl_default_filter}", before any %description block.

%perl_default_filter %{?filter_setup: %{expand: \
%filter_provides_in %{perl_vendorarch}/.*\\.so$ \
%filter_provides_in -P %{perl_archlib}/(?!CORE/libperl).*\\.so$ \
%filter_from_provides /perl(UNIVERSAL)/d; /perl(DB)/d \
%filter_provides_in %{_docdir} \
%filter_requires_in %{_docdir} \
%filter_setup \
}}

