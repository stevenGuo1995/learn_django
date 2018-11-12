

def read_from_file_list_by_readline(path:str):
    """
    从文件中读取文件到Python，使用readline方法，保存格式[[],[],[],]
    :param path: 
    :return: 
    """
    # 定义一个集合
    student_list = []
    # 使用异常处理机制读取文件
    try:
        # 使用with创建和文件关联
        with open(file=path, mode='r', encoding="utf-8-sig") as fd:
            # 读取第一行
            current_student = fd.readline()
            # 使用循环反复读
            while current_student:
                # 把读取的这行数据切割
                temp_list = current_student.strip().replace("\n", "").split(",")
                # 添加到总的集合中
                student_list.append(temp_list)
                # 读取下一行
                current_student = fd.readline()
    except IOError as e:
        print("打开文件出现异常！")
    except UnicodeDecodeError as e:
        print("编码无法识别")
    except Exception as e:
        print("未知的异常！")

    # 返回
    return student_list

def read_from_file_dict_by_readline(path:str):
    # 定义一个集合
    student_list = []
    infos =['sno','sname','gender','birthday','mobile','email','address']
    # 使用异常处理机制读取文件
    try:
        # 使用with创建和文件关联
        with open(file=path, mode='r', encoding="utf-8-sig") as fd:
            # 读取第一行
            current_student = fd.readline()
            # 使用循环反复读
            while current_student:
                # 把读取的这行数据切割
                temp_list = current_student.strip().replace("\n", "").split(",")

                # 定义一个临时的字典
                temp_dict ={}
                # 把数据转为字典类型
                for index in range(len(infos)):
                    temp_dict[infos[index]] = temp_list[index]
                # 添加到集合中

                student_list.append(temp_dict)
                # 读取下一行
                current_student = fd.readline()
    except IOError as e:
        print("打开文件出现异常！")
    except UnicodeDecodeError as e:
        print("编码无法识别")
    except Exception as e:
        print("未知的异常！")

    # 返回
    return student_list

if __name__ == '__main__':
    path="D:\doc\student01.txt"
    print(read_from_file_list_by_readline(path))
    print(read_from_file_dict_by_readline(path))

