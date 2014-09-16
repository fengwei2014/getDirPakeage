getDirPakeage
=============

get directory file names and join some files togeter

打包脚本说明：

必须包含文件：head.txt、endFile.txt、getDirFile.py

Python 2.7.7 版本测试通过，如果不能正常运行，请确认版本

@date:2014.9.16 

@author fengwei

有任何问题及意见联系：QQ:1065538963


1.用编辑器打开getDirFile.py

2.修改参数说明：
	path：目标js文件所在的文件路径（适用于window操作系统）
	projectName：项目名称（默认为：'wms-portal'）
	projectFileOutName：最终输出文件主文件名（默认为：'mywmsportal'）

3.可能更深入修改的参数：
	文本替换规则在  函数： replaceText 中制定
	更多文件合并扩展  	在 fileNameList中添加一项文件，在函数 joinFiles中负责了合并的实现
