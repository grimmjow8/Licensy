<p align="center">
    <img src="https://raw.githubusercontent.com/albertopoljak/Licensy/master/logo.png">
</p>

[![Licensy vAplha](https://img.shields.io/badge/Licensy-alpha-yellow)](#)
[![Invite me!](https://img.shields.io/badge/-Invite%20me-gray?logo=discord)](https://discordapp.com/oauth2/authorize?client_id=604057722878689324&scope=bot&permissions=268446720)
[![Upvote me](https://img.shields.io/badge/-Upvote%20me-7289DA)](https://discordbots.org/bot/604057722878689324)
[![Discord support server](https://img.shields.io/discord/613844667611611332?color=%237289DA&label=Support%20Server&logo=discord)](https://discord.gg/trCYUkz)
[![Activity](https://img.shields.io/github/commit-activity/w/albertopoljak/Licensy)](https://github.com/albertopoljak/Licensy/pulse)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](#)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)](#)
[![License AGPL3](https://img.shields.io/github/license/albertopoljak/Licensy?color=red)](LICENSE.md)

# Licensy - easily manage expiration of roles with subscriptions!

Generate license keys that, when redeemed by a member, will add a certain role to member
that will last for certain time.

Each license is tied to a certain role and certain duration.

When member redeems the license he will get that role for that certain duration.

You can make all of your roles subscribable and each license can have different expiration date.

Members can have unlimited subscriptions active at the same time! (only limited by the Discord role limit per member which is 250).

Works independently with multiple guilds.

## Quickstart bot usage

For full bot usage make sure you have the **administrator** guild permission (or guild owner).

Default prefix is `!`

Default license expiration time is 720h aka 30 days.

After the bot joined the guild call:

```bash
!default_role @role_here
!generate 5
```

First line will set **@role_here** as default guild role.

Second will generate 5 licenses, and as you can see only 5 is a argument so the 
command will use **default** guild role (previously set to **@role_here**) and **default** expiration 
date (which is initially set to 720h aka 30days upon guild join).

If you want to use `!generate` command in some other way (that doesn't rely on using
default guild data but relies on passed arguments) call `!help generate` to see full explanation 
on how to use it.

Quick example for custom `!generate` arguments:

```
!generate 10 @subscription 1m
!generate 5 @supporter 1w
```

This will generate 10 licenses for role `@subscription` in duration of 1 month and 5 licenses for role `@supporter` in
duration of 1 week.

In general these 2 are your friends:

- Call `!help` to see available commands.
Note that you will not see commands that you don't have the permission for.
Example non-admin members will not see admin commands listed when calling help.

- Call `!help command_name` to see additional help for that specific command.
Every command is properly documented.


Optional (so you have more information):

```bash
!guild_info
!faq
```

For any other questions/help/suggestions/anything call `!support` and join the support server :)

You can also join it from this github page, click on the icon at the top of this readme.

## Permissions needed

Note that even if bot has all of these permission he might still not be able to manage some roles:

- Remember that bots role has to be **higher** in role hierarchy than the managed members top role.
Meaning it can only manage roles **below** it's own role in hierarchy.

Bot needs these permissions to operate:

```bash
read_messages=True
```
- Needed so bot can see commands being called, otherwise nothing will happen
when using a command.

```bash
send_messages=True
```
- For sending feedback to guild (success, failure, errors, info)

```bash
manage_roles=True
```
- For actually adding/removing licensed roles from members.

```bash
manage_messages=True
```
- In case there is error while using command that exposes the license your original 
message that is showing license will get deleted to minimize chances of stealing.
This happens for example if you redeem license for a role you **already** have.

## Requirements for source

You need Python 3.6 or later and packages from `requirements.txt`

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, macOS and Windows, packages are available at

  http://www.python.org/getit/

## Quickstart source code

```bash
$ cd Licensy
$ pip install -r requirements.txt
```

Note that discord.py version that was used in development is 1.2.3
, anything above that (except for mayor version changes) should work.

Nevertheless for compatibility reasons the `requirements.txt` will target specifically v1.2.3
but if you are sure that there are no breaking changes in future version feel free to update.

Before running the bot edit the `config.json` found in the root directory.
Adding the token is the most important thing.

After that you are ready to run it:

```bash
$ python3 bot.py
```

Upon startup the bot will create what it needs (if it's missing), this includes:
log file and database file, including folders for them.

Invite the bot to any guild, it will create database guild entry upon joining.

Further steps on how to use the bot are in [Quickstart bot usage](#quickstart bot usage)

## Authors

* **[Joseph Kim](https://github.com/KimchiTastesGood)** - *Original bot and idea*
* **[Braindead](https://github.com/albertopoljak)** - *New bot redesign based on original idea*

## License

This project is licensed under the GNU AGPLv3 License - see the [LICENSE.md](LICENSE.md) file for details
