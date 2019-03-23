Name:          harbour-themepack-breeze-sans
Version:       0.1
Release:       2
Summary:       Breeze Sans font pack
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      harbour-themepacksupport >= 0.8.8-1
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
Breeze Sans package for Theme pack support for Sailfish OS.

%files
%defattr(-,root,root,-)
/usr/share/*

%post
mkdir -p /home/nemo/.themepack/%{name}
if [ -d "/usr/share/%{name}/font" ]; then
	mv /usr/share/%{name}/font /home/nemo/.themepack/%{name}/
	ln -s /home/nemo/.themepack/%{name}/font /usr/share/%{name}/
fi
if [ -d "/usr/share/%{name}/font-nonlatin" ]; then
	mv /usr/share/%{name}/font-nonlatin /home/nemo/.themepack/%{name}/
	ln -s /home/nemo/.themepack/%{name}/ /usr/share/%{name}/
fi

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
    rm -rf /usr/share/{name}
    rm -rf /home/nemo/.themepack/%{name}
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
fi
fi

%changelog
* Sat Oct 27 2018 0.1
- First build.
