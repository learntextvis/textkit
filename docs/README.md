# textkit documentation

## Installing prerequisites

The doc building system has additional requirements past the base `textkit` install.

**Note:** All commands expect you are in the `docs` sub-directory of the project.
So, `cd` to that directory first:

```
cd docs
```

You can install these packages using:

```
pip install -r requirements.txt
```

## Building Docs

This should be done via `make`:

```
make html
```

## Viewing Built Docs

The built documentation should now be in the `_build/html` sub-directory

You can view them by starting a webserver in that directory.

If you are on python 3, this should do that:

```
cd _build/html/; python -m http.server
```

If you are on python 2, try:

```
cd _build/html/; python -m SimpleHTTPServer
```

This should allow you to visit [http://localhost:8000/](http://localhost:8000/) and
see your updated docs.

## Deploying to gh-pages

We are using the [Sphinx Deployment](https://github.com/teracyhq/sphinx-deployment) tooling
to automate deploying documentation to the `gh-pages` branch of this repo.

This keeps the documentation in the same location as the code, which is great for discoverability.

It also provides documentation at a consistent url: [http://learntextvis.github.io/textkit/](http://learntextvis.github.io/textkit/).

I believe Sphinx Deployment is all setup to allow for anyone with write capabilities to the repo
(owners) to update and push documentation with the following commands:

```
make html
make deploy
```

The default deployment is to `gh-pages` which is what we want.
The configuration of the Sphinx Deployment process is specified in `sphinx_deployment.mk` - so check there for all the configuration parameters to ensure everything is set as we want it.

For more info on the options, `README_sphinx_deployment.md` comes from the
