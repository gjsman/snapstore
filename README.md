# Overview

snapstore is a minimalist example of a "store" for snaps, based on the public API specs (https://wiki.ubuntu.com/AppStore/Interfaces/ClickPackageIndex). It allows anyone to host their own collection of snaps for installation on supported platforms.

See http://snapcraft.io for more information on creating and using snap packages.

# Server setup (manual)

Install python-virtualenv.

E.g. on Ubuntu 16.04:
```
sudo apt install python-virtualenv
```

Clone this repo:
```
git clone https://github.com/gjsman/snapstore.git
cd snapstore
```

Setup virtualenv and install dependencies:
```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

Run it:
```
python store.py
```


# File management

Put snaps (named as name.snap) and metadata (named as name.meta) in ./files/ directory. We've already included a few sample snaps.


# Client setup

On any distribution supporting snaps (see http://snapcraft.io), install snapd (requires snapd >=2.0.6).

E.g. on Ubuntu 16.04:
```
sudo apt install snapd
```

Edit /etc/environment, add your store URL, e.g.:
```
SNAPPY_FORCE_API_URL=http://localhost:5000/api/v1/
```

Then restart snapd:
```
sudo service snapd restart
```

# Usage

Supports `snap find <name>`, however `snap install <name>` does not work quite yet.

```
$ snap find
Name      Version  Developer  Notes  Summary
bar       0.2      testuser   -      This is a bar snap
baz       0.4      testuser   -      This is a baz snap
foobar25  2.5      testuser   -      This is a test snap

$ snap find ba
Name  Version  Developer  Notes  Summary
bar   0.2      testuser   -      This is a bar snap
baz   0.4      testuser   -      This is a baz snap

$ snap install bar

Name  Version  Rev  Developer  Notes
bar   2.5      1    testuser   -

$ snap refresh bar

Name  Version  Rev  Developer  Notes
bar   2.5      2    testuser   -
```

# Known issues

This is a fork of an old project from over a year ago. Right now, installing snaps from this snapstore does _not_ work.
However, I are getting close to getting passthrough to work, which will allow you to install this custom store
and still be able to install snaps from the official Snap Store.

The reason this example does not work yet for hosting your own snaps is that we don't support _assertions_ yet.
However, downloading the snap technically works fine, it just won't install. I will work on fixing this, and when
assertions are supported, this snapstore implementation will work.

So, right now, because passthrough and install don't work, you can't actually use this for really anything _yet_.
However, keep watching, and it should be (hopefully) workable soon!

# TODO

- Finish assertion passthrough for official Snap Store (fixing passthrough)
- Figure out assertions for snaps hosted on the open-source Snap Store (this one, far more difficult)
- Maybe a GUI?

