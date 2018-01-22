# manager

- hear alert message on mqtt
- is the only in charge of hot writing into sfera/config collection
- publish update conf
- restart services


### messages

All messages are in
```js
{
  "type": String,
  "data": Object
}
```

### types

###### healt_update

```js
{
  "type": "healt_update",
  "data": {
    "lights" : [ "11:08-11:10",  "21:29-21:32" ],
    "t1" : "5|10|35|45",
    "h1" : "10|20|90|95"
  }
}
```
on success publish on `local/system` message `manager:healt_update`
