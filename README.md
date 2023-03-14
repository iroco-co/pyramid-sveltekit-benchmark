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
