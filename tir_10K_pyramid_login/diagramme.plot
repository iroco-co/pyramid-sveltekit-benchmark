set terminal png size 900, 300
set output "chart.png"

set xdata time
set timefmt "%H:%M:%S"

plot 'postgres_data.csv' using 1:2 with lines title 'PostgreSQL CPU', \
     'python_data.csv' using 1:3 with line title 'Pyramid CPU' 
