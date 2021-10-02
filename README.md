# HyperUBot module's universe
The HyperUBot project extra module repository

Copyright (C) 2020 nunopenim\
Copyright (C) 2020 prototype74

All rights reserved

## What is this?

This is just a repo to keep the sources of the extra modules, that doubles down as the modules-universe for the HyperUBot project. If you are looking for the actual HyperUBot project, [check this](https://github.com/prototype74/HyperUBot) instead!  

## Can I have my files hosted in the official repo?

Right now, since we are still trying to solve some stuff as the Userbot just launched to public, community files are not yet accepted. However in the future, there will be a dedicated telegram group, which a link will be added here. In there you can submit your module, so that we can evaluate the content. If everything is right, and there are no problems at all or suspicious stuff, it will make here!

## Are there any rules to develop to HyperUBot?

Yes there are. The most important step that you should follow is that you should not have commands with the same names as other (official) modules. If however you want to make an extension of a module, say adding commands to an already existing module (a specific example would be `.tban`, temporarily bans a user, as an extension of the admin module), you should create a new module called `admin_ext.py`. Like this, users can keep the stock admin module, and use your extensions. If however you want to improve the algorithm of a specific bot command, you can "root" your bot (by installing the `superuser` extension in modules-universe), to uninstall the admin module from system. Rooting your bot will likely break the updater though, so make your choices wisely.

Secondly, it is also important to mention that if any sort of malicious code has been found while applying to get your files in the module-universe will result in a permanent ban.

The third rule is that the modules in modules-universe cannot break each other (for example, by having the same command names). There is a list of the taken commands, [available here](https://github.com/prototype74/HyperUBot/wiki/Taken-Commands-Reference).

## Developing modules

A small, introductory guide in how to develop your modules can be found [here](https://github.com/prototype74/HyperUBot/wiki/Developing-Modules). This explains the basics in how to setup your module's `.py` file, so that HyperUBot can load it and run it when it is called.

## Hosting your own community repo

To host your own HyperUBot modules repository, for multiple (or not) modules, you will need to drop the `.py` files in a `Release` of your Repo. A full guide in doing this can be found [here](https://github.com/prototype74/HyperUBot/wiki/Community-Repos#how-to-host-your-own-community-repo). In here, we also have some recommendations to follow, such as opening a News Channel about your repo, or how to proceed with external dependencies, in case you need them.

## Licensing

Unless specified on the header of the file, all the components of this repo are licensed under [PEL](https://github.com/nunopenim/module-universe/blob/master/LICENSE.md). A copy of all the Licenses included in this repo can be found under the "Licenses" directory.

