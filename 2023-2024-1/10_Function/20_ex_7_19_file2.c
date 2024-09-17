extern A;
//把file1中定义的外部变量的作用域扩展到本文件
int power(int n)
{
	int i, y = 1;
	for (i = 1; i <= n; i++)
		y *= A;
	return(y);
}
