import angr

project = angr.Project("./babymix", auto_load_libs=False, main_opts={'base_addr':0x00100000})

@project.hook(0x00102225)
def print_flag(state):
    print("FLAG:" , state.posix.dumps(0))
    project.terminate_execution()

project.execute()
