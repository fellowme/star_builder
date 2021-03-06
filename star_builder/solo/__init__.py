from abc import ABC, abstractmethod


class Solo(ABC):
    """
    独立任务程序子任务接口定义
    """
    def __init__(self, **kwargs):
        self.tasks = []

    @abstractmethod
    async def setup(self, *args, **kwargs):
        """
        任务初始化
        :param args:
        :param kwargs:
        :return:
        """

    @abstractmethod
    async def teardown(self, *args, **kwargs):
        """
        资源回收
        :param args:
        :param kwargs:
        :return:
        """

    @abstractmethod
    async def run(self, *args, **kwargs):
        """
        任务执行
        :param args:
        :param kwargs:
        :return:
        """

    @classmethod
    def enrich_parser(cls, sub_parser):
        """
        自定义命令行参数
        :param sub_parser:
        :return:
        """