使用Cross View方式划分NTU RGB+D数据集遇到的缺失值，这个是在查看pyskl仓库NTURGB+D [2D Skeleton]的时候发现的

https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu60_hrnet.pkl

split字段是字典类型，包含xsub_train键、xsub_val键、xview_train键、xview_val键

而xview_train键对应的值发现查看列表长度length的时候遇到了缺失值，于是想把这些缺失值给找出来是哪些？

xview_val键对应的值发现查看列表长度length的时候同样遇到了缺失值，于是想把这些缺失值给找出来是哪些？

process_pkl这个代码就是来找这些缺失值是哪些的
