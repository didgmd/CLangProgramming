void delete_string(char str[], char ch)
//定义外部函数delete_string
{
	int i, j;
	for (i = j = 0; str[i] != '\0'; i++)
		if (str[i] != ch)
			str[j++] = str[i];
	str[j] = '\0';
}
