#############################
Upcoming SELinux Enhancements
#############################

:date: 2015-07-12
:author: Stephanie Lockwood-Childs
:tags: SELinux, security, CIL
:category: news
:slug: selinux_cil
:summary: Upcoming SELinux Enhancements

SELinux userspace policy tools have been undergoing a significant under-the-hood 
design change in order to make local policy customizations much more practical

====================================
Goals of SELinux Userspace Redesign
====================================

SELinux is widely used as part of the security architecture of high-security 
government systems, but its adoption in the commercial space has been hindered
by the difficulty that system administrators have in adapting SELinux policies
for local needs.  This is not entirely surprising, given that SELinux grew out
of government projects for improving security, and typical government processes
require that specialized security experts be in charge of security configurations,
which system administrators maintaining the systems must *not* change. 
In contrast, private companies frequently put their system administrators /
devops staff in charge of implementing security policies on the servers,
and those staff members frequently find SELinux impractical to work with
in a more dynamic commercial environment. Some commercial infrastructures are more 
dynamic than others, but almost all are dynamic compared to the high-security 
certified-at-every-stage environment from which SELinux was born.

The main gaps in SELinux policy maintenance, hindering commercial usage, include:

* lack of mature high-level tools for customizing and reviewing policies
* inability to make certain classes of changes with even low-level tools
* poor support for preserving local changes across system updates

This current incomplete support for maintaining local SELinux customizations
places extra responsibility at the level of policy designer, who should not
merely provide secure defaults, but also foresee what parts of the policy
might need boolean "knobs" for admins to be able to turn them on and off.

======================================
Approach to SELinux Userspace Redesign
======================================

The SELinux maintainers have decided to address the gaps in policy maintenance
by introducing an intermediate language, quite descriptively named 
`Common Intermediate Language (CIL) <CIL_>`_, between the current text policy definitions
and the binary policy format actually loaded the SELinux kernel layer. 

Not surprisingly, CIL supports all core constructs existing in the current 
SELinux policy language, since backward compatibility at a source file level
is being provided via a compiler from the old language to CIL. Thus the initial
deployment of CIL will not require re-writes to all existing SELinux policies,
which should allow a relatively smooth adoption.

Addressing lack of mature high-level policy tools 
-------------------------------------------------

The `current text language <oldlang_>`_ used for defining SELinux policy has not proved
amenable for the development of high-level tools; the current lack of mature
high-level tools is not because high-level tools have never been attempted, but
because they never got good enough to gain wide usage and thus become worth
maintaining in the long-run. Allowing high-level tools to target an
language intentionally designed as an intermediate language is a proven
strategy for efficient support of a variety of frontends; 
see `LLVM Intermediate Representation <llvm_>`_ 
for a shining example of an intermediate language put to good use. 

Addressing limitations in low-level tools
-----------------------------------------

CIL introduces advanced namespace support, including inheritance, which enables
the development of more powerful administration tools. For an example of the
limitations to the current SELinux tools, the existing semanage_ tool can add a
new port label, and subsequently modify or delete its own label, but it can not
override a port label created by the installed policy files. Porting semanage
to work with the policy at the CIL level will allow it to create custom policy
blocks that inherit from the standard policy, but override specific pieces.

Addressing local policy changes and policy updates
--------------------------------------------------

With the pre-CIL SELinux userspace implementation, some changes made it
necessary to `create local policy modules <policydev_>`_ that replaced corresponding default
policy modules. There was no automated method of updating those local
replacement modules to incorporate changes pushed out as an update to the
default policy.

The same CIL features that will allow administrative tools such as semanage 
to become more capable, providing namespaces with inheritance, will also allow
better handling of policy updates by allowing most local changes to be
maintained as specific overrides to the default policy. Unrelated changes
could then be pushed to the default policy and take effect without conflict.

===========================
Early Adopters / Developers
===========================

Those adventurous souls who are interested in following progress in SELinux
policy management by getting their hands dirty with the `latest code from
github <repo_>`_ should consider installing Gentoo for such experiments. 
The Gentoo SELinux team is already preparing to take advantage of 
the upcoming changes, and the team lead Sven Vermeulen has provided 
`live ebuilds <ebuilds_>`_ that allow convenient building of the latest
upstream versions of relevant packages. Sven also provides friendly and 
knowledgeable advice to those working with Gentoo SELinux via the 
`Hardened Gentoo mailing list <hardened_>`_ -- the primary avenue of support 
for new topics such as CIL that are not yet covered by the otherwise excellent 
`Gentoo SELinux documentation <wiki_>`_.

.. _oldlang: http://selinuxproject.org/page/PolicyLanguage#Kernel_Policy_Language_Definition_Links
.. _llvm: https://en.wikipedia.org/wiki/LLVM#LLVM_Intermediate_Representation
.. _CIL: https://github.com/SELinuxProject/cil/wiki
.. _semanage: http://linux.die.net/man/8/semanage
.. _policydev: https://wiki.gentoo.org/wiki/Project:SELinux/Development
.. _repo: https://github.com/SELinuxProject/selinux
.. _ebuilds: http://blog.siphos.be/2015/06/live-selinux-userspace-ebuilds/
.. _hardened: https://wiki.gentoo.org/wiki/Project:Hardened#Participation
.. _wiki: https://wiki.gentoo.org/wiki/SELinux
