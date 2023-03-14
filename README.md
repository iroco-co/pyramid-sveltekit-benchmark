# Benchmark python/pyramid node/sveltekit

## Measure


```
top -b -n 1 | awk 'NR>1 && $12 == "<process_name>" {print strftime("%T"), $1, $9, $10}'
```
