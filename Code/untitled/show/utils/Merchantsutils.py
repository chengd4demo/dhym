from show.models import dhym_support, dhym_process


def get_process(processs):
    print('流程 in ..................................')
    process_list = []
    for processfor in processs:
        process = dhym_process()
        process.id = processfor.id
        process.process_img = '/static/'+str(processfor.process_img)
        process.process_title = processfor.process_title
        process.process_describe = processfor.process_describe
        process_list.append(process)
    print('流程 out ..................................')
    return process_list