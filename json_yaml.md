# JSON  and YAML basics

=============================================================================
### what is JSON
- JSON (JavaScript Object Notation, pronounced /ˈdʒeɪsən/; also /ˈdʒeɪˌsɒn/) 
- is an open standard file format and data interchange format that uses 
- human-readable text to store and transmit data objects consisting of 
- attribute–value pairs and arrays (or other serializable values). 
- It is a common data format with diverse uses in electronic data interchange, 
- including that of web applications with servers.

### what is it for
- JSON is a language-independent data format. It was derived from JavaScript, 
- but many modern programming languages include code to generate and parse 
- JSON-format data. JSON filenames use the extension .json.

### who created it
- Douglas Crockford originally specified the JSON format in the early 2000s.
- He and Chip Morningstar sent the first JSON message in April 2001.

The following example shows a possible JSON representation describing a person.
=============================================================================
```sh

{
  "first_name": "John",
  "last_name": "Smith",
  "is_alive": true,
  "age": 27,
  "address": {
    "street_address": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postal_code": "10021-3100"
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [
    "Catherine",
    "Thomas",
    "Trevor"
  ],
  "spouse": null
}

```

## what is YAML

- YAML (/ˈjæməl/) (see § History and name) is a human-readable 
- data serialization language. It is commonly used for configuration files 
- and in applications where data is being stored or transmitted. 
- YAML targets many of the same communications applications as 
- Extensible Markup Language (XML) but has a minimal syntax which 
- intentionally differs from Standard Generalized Markup Language (SGML). 
- It uses both Python-style indentation to indicate nesting, 
- and a more compact format that uses [...] for lists and {...} for maps 
- but forbids tab characters to use as indentation 
- thus only some JSON files are valid YAML 1.2.

```sh
- Custom data types are allowed, but YAML natively encodes scalars 
(such as strings, integers, and floats), lists, and associative arrays 
(also known as maps, dictionaries or hashes). These data types are based on 
the Perl programming language, though all commonly used high-level programming 
languages share very similar concepts.[6][7][8] The colon-centered syntax, 
used for expressing key-value pairs, is inspired by electronic mail headers 
as defined in RFC 822, and the document separator --- is borrowed from MIME (RFC 2046). 
Escape sequences are reused from C, and whitespace wrapping for 
multi-line strings is inspired by HTML. 
Lists and hashes can contain nested lists and hashes, forming a tree structure; 
arbitrary graphs can be represented using YAML aliases (similar to XML in SOAP).
YAML is intended to be read and written in streams, a feature inspired by SAX.

```

## example of YAML file

```sh
---
receipt:     Oz-Ware Purchase Invoice
date:        2012-08-06
customer:
    first_name:   Dorothy
    family_name:  Gale

items:
    - part_no:   A4786
      descrip:   Water Bucket (Filled)
      price:     1.47
      quantity:  4

    - part_no:   E1628
      descrip:   High Heeled "Ruby" Slippers
      size:      8
      price:     133.7
      quantity:  1

bill-to:  &id001
    street: |
            123 Tornado Alley
            Suite 16
    city:   East Centerville
    state:  KS

ship-to:  *id001

specialDelivery:  >
    Follow the Yellow Brick
    Road to the Emerald City.
    Pay no attention to the
    man behind the curtain.
...
```



