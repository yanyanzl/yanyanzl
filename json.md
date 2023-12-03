# JSON basics

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