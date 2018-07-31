# Collective Sidebar

Collective Sidebar is a minimalist and modern toolbar and header replacement for Plone. It functions independently of any theming and works as a direct replacement for the default toolbar. Simply install the add-on to see the results instantly..!

## Features

* [Enable / Disable] Site cover when sidebar is open
* [Changeable] Header and navigation primary colour
* [Enable / Disable] Navigation sections
  * Profile section
* Plone LiveSearch integrated into navigation
* [Enable / Disable] Navigation effects
  * `box-shadow` effects
* Navigation can be locked open for continuous editing
* Navigation sections collapsable when logged-in
* Implements CSS3 transform 3D optimisation
* Header and navigation are fixed, no need to scroll back up!
* Patches the default Plone portrait size and quality
* Patches the default Plone main template, keeping the clutter at bay...

## Todo

* Integrate `mockup-patterns-structure` into navigation for `folder_contents` syncing
* Allow profile section to be moved into the header
* Allow navigation to be left aligned as opposed to be being right aligned
* Allow navigation itself to be themed independently with configuration, including navigation background itself...
* Integrate font icon switcher, or include multiple font icon packs that can be selected on-the-fly
* Integrate animated burger icon, possibly even a few that can be selectable...
* Fix header logo, currently it's only the Plone logo, though this can be changed in the template relatively easily

## Screenshots

### Toolbar

![Toolbar](http://i.imgur.com/OZplA80.png)

### Header

![Header](http://i.imgur.com/Vr7bVUy.png)

## Examples

- https://www.actionbike.de
- https://www.operun.de

## Translations

* English (en)
* Deutsch (de)

## Installation

Add the `collective.sidebar` package to your buildout...

    [buildout]

    ...

    eggs =
        collective.sidebar


...and then run ``bin/buildout``.

## Contribute

* Issue Tracker: https://github.com/collective/collective.sidebar/issues
* Source Code: https://github.com/collective/collective.sidebar
* Documentation: https://docs.plone.org/foo/bar

## License

The project is licensed under the GPLv2.

## Credits

This project uses JAM icons: https://github.com/michaelampr/jam
