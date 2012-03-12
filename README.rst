==========
In One Ear
==========

As a great scientist once said, "Please excuse the crudity of this model; I
didn't have time to build it to scale or to paint it."

In One Ear is a toy blog, a chance for me to find out what it's like to start a
Django site from scratch as opposed to my usual ENORMOUS INDUSTRIAL-STRENGTH
MOZILLA CUSTOM-LIBRARY BOOGIE TOWN fare.

Beyond the bare-bones stuff, it has...

* Nose test integration, using django-nose (because I'll go nuts without it)
* Model makers for tests (because I still hate fixtures)
* Internationalized static text (because it's easy)
* Admin support for Articles and Comments (because it made bootstrapping easier)
* Just enough CSS to make it bearable (because it's late and I am tired)


Known Issues
============

* We allow saving invalid ReST. Rendering reports the errors (and doesn't foul
  the document), but it would be nice to hook that into the form validation.
* Excerpting of articles that have ReST errors (or just use fancy structures)
  might output invalid HTML on the front page. Tags are balanced, thanks to
  ``truncatewords_html``, but it's possible to, for instance, end up with a
  ``dl`` with a ``dt`` but no ``dd``. Excerpting ReST is fun.
* I see too late that Django has its own comments system. Using that would have
  given this a little bit of spam resistance for free.


Future
======

* The front page would likely be the most commonly hit page, but it does a lot
  of computation at the moment. All that excerpting of article bodies means a lot
  of parsing. We should cache either the individual excerpts or maybe even entire
  rendered pages. If the latter, maybe that should happen in some reverse proxy.
* Comment editing (maybe not anonymous ones)
* Flip over to HTTPS when logging in, and stay there until logged out.
* Minify static assets.
* Support a CDN.
* Nice 403s
