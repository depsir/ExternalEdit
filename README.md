#Description
This simple plugin implements the interface for external editing a mediawiki page into SublimeText2

Every page can be edited externally by attaching '&externaledit=true' to the edit link, for example

    http://en.wikipedia.org/w/index.php?title=MediaWiki&action=edit&externaledit=true

Refer to http://www.mediawiki.org/wiki/Manual:External_editors

This code is partyl based on http://code.google.com/p/python-wikitools/

#Installation
Go to your packages directory which usually is ~/.config/sublimetext2/Packages

    git clone https://github.com/depsir/ExternalEdit

#Configuration
In your Preferences: Settings - User, accessible from the command palette (ctrl+shift+p) add these two lines

    "externaledit_username": "username",
    "externaledit_password": "password"

Note that every line except the last one must end with a comma

#Usage
1. Go to an external edit link, a file will be downloaded. Its name should be something like index.php
1. The mediawiki file will be downloaded and shown into sublime text
    1. if the file name was something like index.php the page will be downloaded automatically
    1. otherwise just run the "ExternalEdit: Load control file" command
1. From the command palette (ctrl+shift+p) run the "ExternalEdit: Save changes" command

#Contributing
1. Fork it
1. Create your feature branch (git checkout -b my-new-feature)
1. Commit your changes (git commit -am 'Added some feature')
1. Push to the branch (git push origin my-new-feature)
1. Create new Pull Request

