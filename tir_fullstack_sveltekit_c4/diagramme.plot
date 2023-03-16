set terminal png size 900, 300
set output "chart.png"

set xdata time
set timefmt "%H:%M:%S"

set title 'Test fullstack 4 clients'
set xlabel "Temps"
set ylabel "% CPU"

plot 'new-postgresql.csv' using 1:2 with lines title 'Node PostgreSQL CPU', \
     'new-server.csv' using 1:3 with line title 'Nodejs CPU', \
     '../tir_fullstack_pyramidsvelte_c4/postgresql.csv' using 1:2 with line title 'Python PostgreSQL CPU', \
     '../tir_fullstack_pyramidsvelte_c4/server.csv' using 1:3 with line title 'Pyramid CPU' 
