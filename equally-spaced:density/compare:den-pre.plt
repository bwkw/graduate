set term pdf
set out "compare:den-pre.pdf"
set xlabel "density"
set ylabel "pressure"
set xlabel font "Arial,15"
set ylabel font "Arial,15"
#ticsはメモリ文字
set tics font "Arial,10"
#keyは凡例
set key font"Arial,16"
set key left top
plot "compare:den-pre.dat" u 1:2 with lines title "理論値", "compare:den-pre.dat" u 1:3 with lines title "測定値"
