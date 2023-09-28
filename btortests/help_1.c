#include<stdlib.h>
#include<wait.h>
 
int main()
{
    char *s=NULL;
    int n=0;//控制父子进程的次数
    
    pid_t id=fork();
    assert(id!=-1);
    
    if(id==0)//子进程
    {   
        s="child";
        n=7;
    }   
    else
    {   
        s="parent";
        n=3;
        int val=0;
        if(WIFEXITED(val))//如果正常退出
        {
            printf("val=%d\n",WEXITSTATUS(val));
        }
        wait(&val);
        printf("val=%d\n",val);
    }   
    //父子进程一起运行
    int i=0;
    for(;i<n;i++)
    {   
        printf("s=%s ,pid=%d ,ppid=%d n的地址=%p n=%d\n",s,getpid(),getppid(),&n,n);
        sleep(1);
    }   
    exit(0);
}