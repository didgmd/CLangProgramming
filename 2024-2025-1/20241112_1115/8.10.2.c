void sort(int *x, int n) // 形参x是指针变量
{
    int i, j, k, t;
    for (i = 0; i < n - 1; i++)
    {
        k = i;
        for (j = i + 1; j < n; j++)
            if (*(x + j) > *(x + k))
                k = j; //*(x+j)就是x[j]，其他亦然
        if (k != i)
        {
            t = *(x + i);
            *(x + i) = *(x + k);
            *(x + k) = t;
        }
    }
}
