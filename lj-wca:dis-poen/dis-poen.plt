set term pdf
set out "dis-poen.pdf"
set xrange [0:]
set yrange [-1:8]
set xlabel "density"
set ylabel "pressure"
set xlabel font "Arial,10"
set ylabel font "Arial,10"
#ticsはメモリ文字
set tics font "Arial,10"
#keyは凡例
set key font"Arial,10"
plot "dis-poen.dat" u 1:2 with lines title "wca", "dis-poen.dat" u 1:3 with lines title "lj"
