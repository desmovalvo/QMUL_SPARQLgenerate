# SPARQLgenerate service

This is a simple web server that provides access to the [SPARQL Generate](https://ci.mines-stetienne.fr/sparql-generate/) service. The original service is provided by École des Mines de Saint-Étienne. The present project is only a convenience wrapper.

## How to use it?

Simply start the server with:

```
$ python3 sparqlgen.py
```

And then issue your request with an HTTP POST with a JSON dict containing the key `query` with your SPARQL generate query as value.

## An example?

An example file is provided. It performs a query on Jamendo (so you need a jamendo key to use it) and maps the results according to the AudioCommons ontology. The first argument is the jamendo token, the second is your search pattern:

```
$ python3 example.py <JAMENDO_TOKEN> <SEARCH_PATTERN>
```

## License

This very simple script is released under GNU GPL v3.0. Enjoy!