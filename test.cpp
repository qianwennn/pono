#include <bits/stdc++.h>
using namespace std;
int main()
{
	vector <int> v;
	v.push_back(5);
	v.push_back(7);
	v.push_back(2);
	v.push_back(1);
	vector<int>::iterator it;
	for(it = v.begin(); it != v.end(); it++)
		cout << it << endl;
	cout << "容器中第一个元素是：" << *v.begin() << endl;
	cout << "容器中最后一个元素是：" << *(--v.end()) << endl;
}


