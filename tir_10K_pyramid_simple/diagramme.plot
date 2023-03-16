set terminal png size 900, 300
set output "chart.png"

set xdata time
set timefmt "%H:%M:%S"

plot 'postgresql.csv' using 1:2 with lines title 'PostgreSQL CPU', \
     'server.csv' using 1:3 with line title 'Nodejs CPU' 
