OTRS - Ticket Request System
============================

`OTRS`_ is a Ticket Request System (also well known as trouble ticket
system) with many features to manage customer telephone calls and
e-mails. The system is built to allow your support, sales, pre-sales,
billing, internal IT, helpdesk, etc. department to react quickly to
inbound inquiries.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- OTRS configurations:
   
   - Installed from package management.
   - Includes spell checking and documentation.

- SSL support out of the box.
- Includes TurnKey web control panel (convenience).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, MySQL, Postfix and Procmail

Customer registration requires valid networking configuration (email
support).

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH, MySQL: username **root**
-  OTRS: username **admin**


.. _OTRS: http://otrs.org
.. _TurnKey Core: https://www.turnkeylinux.org/core
