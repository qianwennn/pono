import subprocess
import time


def execute_cmd(cmd, remote=None, timeout=5):
    """
    @param cmd: 传入要执行的命令
    @param remote:  要远程执行的机器节点  host或者ip， 不传入remote认为是本地执行
    @param timeout: 命令自动结束的超市时间 默认5s
    @return: （退出码，命令正常输出，error信息）
    """
    t_beginning = int(time.time())
    try:
        if remote:
            ret = subprocess.Popen("ssh " + remote + " " + cmd, shell=True, close_fds=True,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            ret = subprocess.Popen(cmd, shell=True, close_fds=True, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        # logger.error("cmd:{}, node:{}, err_msg:{}".format(cmd,node,e),exc_info=True)
        return 256, "", e
    if ret:
        stdout, stderr, task_break = "", "", False
        try:
	        while True:
	            # 判断是否命令是否结束
	            if ret.poll() is not None:
	                break
	            seconds_passed = int(time.time()) - t_beginning
	            # 超时判断，超时即退出并记录日志 
	            if timeout and seconds_passed > timeout:
	                ret.terminate()
	                # logger.error("task is break by timeout,cmd:{},timeout:{}".format(cmd, timeout))
	                task_break = True
	                break
	            time.sleep(0.1)
	            # 每次循环把存在pipe里面的数据读出来，防止数据量太多，pipe放不下，导致最后返回的stdout数据是被截断的
	            tmp_stdout, tmp_stderr = ret.communicate()
	            stdout += tmp_stdout
	            stderr += tmp_stderr
	        if task_break:
	            stderr = "task is break by timeout,cmd:{},timeout:{}".format(cmd, timeout)
	    except KeyboardInterrupt:
            print "\n进程已手动中断，pid:{}".format(ret.pid)
            return 256, "", ""
        finally:
            ret.stdout.close()
            ret.stderr.close()

        return ret.returncode, stdout, stderr
