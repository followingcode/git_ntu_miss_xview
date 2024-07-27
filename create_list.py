import os
import re

from pyskl.smp import mwlines

def writeList(dirpath, name):
    path_train = os.path.join(dirpath, 'Train')
    path_test = os.path.join(dirpath, 'Test')
    trainfile_list = os.listdir(path_train)
    testfile_list = os.listdir(path_test)

    train = []
    for train_name in trainfile_list:
        train_dict = {}
        sp = train_name.split('A')
        if len(sp) >= 2:
            train_dict['vid_name'] = train_name
            action_id = re.findall(r'\d+', sp[1])
            if action_id:
                action_id = int(action_id[0])
                train_dict['label'] = action_id - 1
            else:
                train_dict['label'] = None
        train.append(train_dict)

    test = []
    for test_name in testfile_list:
        test_dict = {}
        sp = test_name.split('A')
        if len(sp) >= 2:
            test_dict['vid_name'] = test_name
            action_id = re.findall(r'\d+', sp[1])
            if action_id:
                action_id = int(action_id[0])
                test_dict['label'] = action_id - 1
            else:
                test_dict['label'] = None
        test.append(test_dict)

    # 对 train 和 test 列表分别进行排序
    train.sort(key=lambda x: x['vid_name'])
    test.sort(key=lambda x: x['vid_name'])

    # 将 train 和 test 列表合并到 lines 列表中
    lines = [(os.path.join(path_train, x['vid_name']) + ' {}').format(x['label']) for x in train] + \
            [(os.path.join(path_test, x['vid_name']) + ' {}').format(x['label']) for x in test]

    mwlines(lines, name)

writeList(r'/root/autodl-tmp/Cross-View', '/root/pyskl/until/xview_train_test_total.list')