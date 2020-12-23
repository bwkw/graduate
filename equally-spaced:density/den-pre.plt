set term pdf
set out "den-pre.pdf"
set xlabel "{/Arial-Italic ρ}"
set ylabel "{/Arial-Italic P}"
set xlabel font "Arial,15"
set ylabel font "Arial,15"
#ticsはメモリ文字
set tics font "Arial,10"
#keyは凡例
set key font"Arial,16"
set key left top
plot "compare:den-pre.dat" with lines linewidth 3 title "測定値"
