# semcal

Combining the concepts of `semver` and `calver`.  Give semcal a `semver` and it'll tell you what it's `calver` would be.

Do an HTTP GET (e.g. in a browser) a URL of the form:

`<language>.semcal.org/<package>[==<semver>]`

and get back a `calver` string.

e.g.:

`python.semcal.org/requests==2.21.0`

returns a `calver` version string:

`2018.12`

If you don't provide a `==<semver>`, the most recent version will be used.

