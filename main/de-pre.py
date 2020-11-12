#av_preファイルを読み込み、de-preファイルを作成

for i in range(11):
    r = 10 + i/10
    filename = "de-pre.dat"
    loadfile = "L{}-av_pre.dat".format(r)
    with open(filename, "a")as f:
        with open(loadfile) as lf:
            for line in lf:
                f.write(line)
                f.write("\n")
