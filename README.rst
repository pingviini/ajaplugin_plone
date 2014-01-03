Deploy Plone buildouts with Aja
===============================

.. image:: https://secure.travis-ci.org/pingviini/ajaplugin_plone.png
    :target: http://travis-ci.org/pingviini/ajaplugin_plone

Configuration
-------------

ajaplugin_plone looks config from section 'deploy:plone'. Currently available
options are:

ignores
    Newline separated globs telling which files/directories are excluded
    during deployment. This list is appended to Aja's global ignores list.

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


