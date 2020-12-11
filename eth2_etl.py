#!usr/bin/python3
import service.api_service as api
import time
import cli


def vld_task(epoch):
    begin_time = time.time()
    print('begin')
    print(api.get_validator(epoch))
    print(f'time cost on {epoch} is {time.time() - begin_time}s')


if __name__ == '__main__':
    cli.cli()
