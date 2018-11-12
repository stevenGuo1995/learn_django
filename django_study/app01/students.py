import pymysql


def read_file(filepath: str):
    student_list = []
    infos = ['sno', 'sname', 'gender', 'birthday', 'mobile', 'email', 'address']
    # 使用异常处理机制读取文件
    try:
        # 使用with创建和文件关联
        with open(file=filepath, mode='r', encoding="utf-8-sig") as fd:
            # 读取第一行
            current_student = fd.readline()
            # 使用循环反复读
            while current_student:
                # 把读取的这行数据切割
                temp_list = current_student.strip().replace("\n", "").split(",")

                # 定义一个临时的字典
                temp_dict = {}
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
    print(read_file(r'students.txt'))
