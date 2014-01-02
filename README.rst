Deploy Plone buildouts with Aja
===============================

Configuration
-------------

ajaplugin_plone looks config from section 'deploy:plone'. Available options
are:

* ignores (newline separated globs).


Example
-------

Here is example of the possible configuration::


    [deploy:plone]
    ignores =
        *.old
        *.fs
        *.pid
        *.lock
        var/filestorage
        var/blobstorage


