#!/usr/bin/python3

# reqs
import sys
import yaml
import requests

# main
if __name__ == "__main__":

    # jamendo token and search pattern must be specified as arguments
    if len(sys.argv) != 3:
        print("Usage: python3 example.py JAMENDO_TOKEN SEARCH_PATTERN")
        sys.exit()

    # read parameters
    jamToken = sys.argv[1]
    pattern = sys.argv[2]
    
    # read the file containing mappings
    example = yaml.load(open("example.yaml", "r"))
    query = example["jamendoMapping"] % (jamToken, pattern)
    print("Sending the following SPARQL generate query:")
    print(query)
    
    # create and configure a request
    data = {"query": query  }
    response = requests.post('http://localhost:5000/sparqlgen', data=data)
    print("Response:")
    print(response.text)
