# Benchmark python/pyramid node/sveltekit

## Measures

For the python/sveltekit process we do : 

```
while true; do sleep 2; top -b -n 1 | awk 'NR>1 && $1 == 30002 {print strftime("%T"), $1, $9, $10}' | tee -a server.txt; done
```

For the postgreql docker container : 

```
while true; do docker stats --no-stream | grep postgresql | awk '{print strftime("%T"),$3, $7}'| tee -a postgresql.txt; done
```

## Injector

For python it is ajax : 

```shell
ab -n 10000 -c 4 -p login.json -T 'application/json'  192.168.1.3:5173/api/signin
```

with login.json :

```json
{"email":"test@iroco.co","password":"pass"}
```


For svelte we have to post the form

```shell
$ ab -n 10  -p login.form -T 'application/x-www-form-urlencoded' -H 'Origin: http://192.168.1.3:3000'  http://192.168.1.3:3000/

```

with login.form :

```
email=test@iroco.co&password=pass
```

It was not working because of the end of line `0a` line feed character. We had to remove it with : 

```shell
$ truncate -s -1 login.form
```
