Status: draft
Title: Everything you ever wanted to know about Heartbleed (but were afraid to ask)
Date: 2014-04-25 23:40
Tags: heartbleed, heartbeat, openssl, ssl, security, encryption
Category: security
Slug: heartbleed
Author: Donald Burr
Summary: A synopsis of the "Heartbleed" bug in OpenSSL, and what you need to know to keep yourself safe and secure, both as a user as well as an administrator.

# Everything you ever wanted to know about Heartbleed (but were afraid to ask)
### Cutting through the FUD to bring you "just the facts, ma'am"
#### by Donald Burr

---

Unless you live in a monastery deep in the Himalayas or something, you have by now heard of the "Heartbleed" bug that affects X percent of the world's web servers.  But, as it is foten wont to do, the media has failed to report on some aspects of Heartbleed while it has exaggerated others to the point of hyperbole.  In this article I hope to clear up some of the FUD and cut to the core of exactly what you,as a web user as well as a server administrator, need to know about Heartbleed.

[CVE-2014-0160][CVE] aka [Heartbleed][HEARTBLEED].

What is the Heartbleed bug?

Heartbleed is a bug that affects the popular OpenSSL cryptographic library.  It was introduced  affects openssl 1.0.1 released march 2012 through 10.1f
it was correct in 1.01.g released apr 7

How does it work?

Was the NSA behind it?

With the contnuing release of leaked documents coming from Edward Snowden, it's natural to wonder whether Heartbleed was somehow engineered by the NSA or other shadowy government organizations. Well, the general consensus of the Internet seems to be "no." In fact, it has all the appearances of a perhaps ill-thought-out commit by a
Introduced dec 31 2011 in

What to do as a user
- people say change passwords, DO NOT until the server cert has been reissued
- instructions on how to activate certificate revocation check
- THEN change y our password

What to do as a server admin
- upgrade openssl, duh
- revoke your ssl certificate and get a new one issued (depending on how tinfoil hat you are)

does not just affect web servers
affects anything using openssl - most notably, openssh and openvpn
regen your keys, reissue vpn certs, etc.


Which platforms are affected, and which aren't
windows is unaffected, they use their own ssl libraries
mac system level apps are unaffected, they use their own ssl libraries. HOWEVER if yuo have installed custom softwre using fink, macports or homebrew some of that software may have been compiled against its own version of openssl.  check your package mnager and upgrade if necessary.
however some airport base stations may be affected check your airport utility for update info
linux definitely affected, check which version of openssl is installed
ios is unaffectd, being an apple product it is using apple's libraries
android IS affected, not system level but app level???  heartbleed scanners are crap, don't trust them (and may be viruses themselves!)



this is scary because it affects key infrastructure software
prompted a code review similar in the style of the truecrypt review
already two projects(?) have come out: libressl tore out chunks of legacy code,
here's also gnutls, but they have had their own issues
beware of "new" code









Be sure and mention:

* [SSL Labs Heartbleed server tester][SSLLABS]
* Browser test for Heartbleed - plugins? site with info?
* List of sites that are known to be affected
* It's not as bad as some people are making it out to be
* What can be leaked - server SSL cert keys, usernames/passwords, etc.
* Browser certificate revocation - need to make sure this is enabled!
* affects more than web servers, affects anything that links against openssl, e.g. ssh, openvpn, ...

---

*[Donald Burr][DBURRBLOG] has been using -- and abusing -- computers and gadgets practically since the day he was born.  (Rumor has it he was born with a keyboard in one hand and a mouse in the other.)  He is an [avid amateur app developer][DBURRAPPS] and is [available for hire][CONTACT] if you need a little help getting started in app writing.  When he's not geeking around with tech, he can be found blogging and podcasting about Japanese animation and culture at [Otaku no Podcast][OTAKU].  He can be found on the Twitters as [@dburr][DBURRTWITTER].*

[CVE]: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160 "CVE-2014-0160"
[HEARTBLEED]: http://heartbleed.com "Heartbleed information site"
[SSLLABS]: https://www.ssllabs.com/ssltest/ "SSL Labs Server Tester"
[DBURRBLOG]: http://DonaldBurr.com/ "Donald Burr's Blog"
[DBURRAPPS]: http://DonaldBurr.com/apps/ "Donald Burr's Apps"
[CONTACT]: http://donaldburr.com/contact-me/ "Contact Me"
[OTAKU]: http://otakunopodcast.com/ "Otaku no Podcast"
[DBURRTWITTER]: http://twitter.com/dburr/ "Donald Burr on Twitter"
