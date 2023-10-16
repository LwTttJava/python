from Bio.Seq import Seq


# 序列(Seq) 示例
# 通常通过文件读取序列，但是也可以用过字符串直接创建序列

def no_init_data_seq_error():
    """
    Seq 序列内容未定，长度已知，使用Seq会报错
    :return:
    """
    # Seq对象的创建支持两个传参，data和长度
    my_undefined_sequence = Seq(None, 20)
    # data未指定数据，所以使用就会报错  Bio.Seq.UndefinedSequenceError: Sequence content is undefined
    print(my_undefined_sequence)


def init_data_seq_test_01():
    """
    创建序列，通过序列（）
    :return:
    """
    # 创建一个序列对象 , data - Sequence, required (string)
    my_seq = Seq("TTGGCCATTGTAATGGGCCGC")
    print(my_seq)

def use_dictionary_init_part_seq():
    """
       If the sequence contents is known for parts of the sequence only, use
       a dictionary for the data argument to pass the known sequence segments:
    :return:
    字典参数说明            {index:"已知序列"}
    """
    my_partially_defined_sequence = Seq({0: "ACGT"}, 10)
    print(len(my_partially_defined_sequence))

    # 数据截取 列表索引[0,4) ,只能使用已知的序列
    print(my_partially_defined_sequence[0:4])

if __name__ == '__main__':
    # 多行注释 CTRL + /
    # no_init_data_seq_error()
    # init_data_seq_test_01()
    # use_dictionary_init_part_seq()
    pass

