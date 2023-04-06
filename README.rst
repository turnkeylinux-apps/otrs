OTRS - Ticket Request System
============================

`((OTRS)) Community Edition`_ is a Ticket Request System (also well known as
trouble ticket system) with many features to manage customer telephone calls
and e-mails. The system is built to allow your support, sales, pre-sales,
billing, internal IT, helpdesk, etc. department to react quickly to
inbound inquiries.

Please note: as of TurnKey v17.0, OTRS upstream has now gone closed source,
and the "Community Edition" appears unmaintained. So our OTRS appliance
installs the `Znuny` fork of "((OTRS)) Community Edition". As such, this
appliance will be renamed to "Znuny" at some point in the future.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- OTRS/Znuny configurations:
   
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
-  OTRS/Znuny: username **root@localhost**


.. _((OTRS)) Community Edition: https://otrscommunityedition.com/
.. _Znuny: https://www.znuny.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
