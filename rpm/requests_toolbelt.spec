#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
#

Name:       requests_toolbelt

# >> macros
BuildArch: armv7hl
# << macros

Summary:    requests_toolbelt python3 module
Version:    0.4.0
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
Requires:   requests
%description
requests_toolbelt python3 module build for sailfishos


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/lib/python3.4/site-packages/
cp -r requests_toolbelt %{buildroot}/usr/lib/python3.4/site-packages/
# << install pre

# >> install post
# << install post

%pre
# >> pre
# << pre

%preun
# >> preun
# << preun

%files
%defattr(-,root,root,-)
/usr/lib/python3.4/site-packages
# >> files
# << files
