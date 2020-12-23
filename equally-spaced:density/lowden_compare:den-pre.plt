set term pdf
set out "lowden_compare:den-pre.pdf"
set xlabel "{/Arial-Italic ρ}"
set ylabel "{/Arial-Italic P}"
set xlabel font "Arial,15"
set ylabel font "Arial,15"
set xrange [0:1]
set yrange [0:1]
#ticsはメモリ文字
set tics font "Arial,10"
#keyは凡例
set key font"Arial,16"
set key left top
plot "lowden_compare:den-pre.dat" u 1:2 with lines linewidth 3 title "理論近似値", "lowden_compare:den-pre.dat" u 1:3 with lines linewidth 3 title "測定値"