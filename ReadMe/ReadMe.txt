文件夹说明：
SidenyUITest
--ConfigMethod                      存放布局文件与各类地址
--Data                              存放数据，例如参数化的Excel
--Drivers                           存放各类selenium webdriver
--Log                               存放日志
--Others                            其他一些文件的存放
--ReadMe                            说明
--Report                            生成报告的存放处
--TestCase

----Case                            用例
----Common                          封装过的通用方法
----Interface                       接口
----Page                            封装过的页面
----Suite                           测试套件用来组织测试用例

--Utils                             公共方法


经过从网上查找资料，发现网上大多资料为python2.7，通过本人的调整已经完全可以适配python3.7。
但是，执行用例时,使用 if __name__ == '__main__': 始终无法实现将生成的文件正确放置到规定的位置，
所以执行用例时选用的是unittest的方法。