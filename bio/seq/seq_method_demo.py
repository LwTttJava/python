from Bio.Seq import Seq

if __name__ == '__main__':
    my_dna = Seq("-ATA--TGAAAT-TTGAAAA")
    # 去掉间隙字符
    print(my_dna.replace())